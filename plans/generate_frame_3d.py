# -*- coding: utf-8 -*-
"""
Fauteuil de transfert médical — Squelette 3D SolidWorks
========================================================
Génère automatiquement le squelette fil-de-fer du cadre tubulaire
dans SolidWorks via l'API win32com.

Utilisation :
  1. Ouvrir SolidWorks (ou laisser le script l'ouvrir)
  2. Activer l'environnement Anaconda : conda activate env_these
  3. Exécuter : python generate_frame_3d.py
  4. Dans SolidWorks : Weldments > Pièces soudées > Élément structurel
     Standard : ISO | Type : Square Tube | Taille : 30x30x2

Auteur : Karim Zennadi — ENP Alger — Open Lab v0.1
"""

import sys
import pythoncom
import win32com.client

# ══════════════════════════════════════════════════════════════════
#  DIMENSIONS DU CADRE (toutes en mètres — unité interne SW API)
# ══════════════════════════════════════════════════════════════════

# Gabarit général
W_EXT       = 0.620   # Largeur extérieure totale (hors-tout)
HS          = 0.500   # Hauteur d'assise depuis le sol
HH          = 0.950   # Hauteur des poignées de poussée
LS          = 0.420   # Profondeur du siège (avant ↔ arrière)

# Géométrie des roues
H_AXLE_REAR = 0.100   # Hauteur axle roue arrière (Ø200mm → r=100mm)
H_AXLE_FRONT= 0.075   # Hauteur axle roue avant  (Ø150mm → r=75mm)

# Repose-pieds
Y_FOOTREST  = LS + 0.10   # 10 cm en avant du pied avant
H_FOOTREST  = 0.080       # Hauteur repose-pieds depuis sol

# Accoudoirs
H_ARMREST   = HS + 0.230  # 23 cm au-dessus du siège (= 730mm du sol)
Y_ARM_FRONT = LS - 0.050  # 5 cm en retrait du pied avant
Y_ARM_REAR  = 0.020       # 2 cm en avant du pied arrière

# Poignée légèrement en retrait de l'axe arrière
Y_HANDLE    = -0.050

# Positions X des cadres gauche / droit
X_L = -(W_EXT / 2)   # = -0.310 m  (cadre gauche)
X_R =  (W_EXT / 2)   # = +0.310 m  (cadre droit)

# Positions Y longitudinales
Y_REAR  = 0.000   # Pied arrière / axle arrière
Y_FRONT = LS      # Pied avant   / axle avant


# ══════════════════════════════════════════════════════════════════
#  FONCTIONS UTILITAIRES
# ══════════════════════════════════════════════════════════════════

def connect_solidworks():
    """Se connecte à SolidWorks (ouvre l'appli si nécessaire)."""
    pythoncom.CoInitialize()
    try:
        app = win32com.client.GetActiveObject("SldWorks.Application")
        print("[OK] SolidWorks déjà ouvert — connexion établie.")
    except Exception:
        app = win32com.client.Dispatch("SldWorks.Application")
        app.Visible = True
        print("[OK] SolidWorks lancé.")
    return app


def find_part_template(app):
    """Cherche le template Part.prtdot dans les emplacements SolidWorks."""
    import glob, os

    # 1. Préférence utilisateur
    t = app.GetUserPreferenceStringValue(9)
    if t and os.path.isfile(t):
        return t

    # 2. Recherche dans ProgramData et Program Files
    patterns = [
        r"C:\ProgramData\SolidWorks\**\Part.prtdot",
        r"C:\Program Files\SOLIDWORKS Corp\**\part.prtdot",
        r"C:\Program Files\SOLIDWORKS Corp\**\Part.prtdot",
        r"C:\Program Files\SolidWorks Corp\**\Part.prtdot",
    ]
    for pat in patterns:
        hits = glob.glob(pat, recursive=True)
        if hits:
            return hits[0]

    # 3. Demande à l'API le dossier de templates
    folder = app.GetUserPreferenceStringValue(15)  # swDefaultTemplateLocation
    if folder:
        for name in ("Part.prtdot", "part.prtdot"):
            p = os.path.join(folder, name)
            if os.path.isfile(p):
                return p

    raise RuntimeError(
        "Template Part.prtdot introuvable.\n"
        "Dans SolidWorks : Options > Emplacements des fichiers > Modèles de documents\n"
        "Copiez le chemin affiché et passez-le en argument : python generate_frame_3d.py <chemin>"
    )


def new_part(app):
    """Crée un nouveau document Part."""
    if len(sys.argv) > 1:
        template = sys.argv[1]   # chemin passé en argument
    else:
        template = find_part_template(app)

    print(f"    Template : {template}")
    doc = app.NewDocument(template, 0, 0, 0)
    if doc is None:
        raise RuntimeError("Impossible de créer un nouveau document Part.")
    doc.SetSaveFlag()
    print("[OK] Nouveau document Part créé.")
    return doc


def draw_line(sk, x1, y1, z1, x2, y2, z2):
    """Trace une ligne dans le sketch 3D actif."""
    sk.CreateLine(x1, y1, z1, x2, y2, z2)


# ══════════════════════════════════════════════════════════════════
#  GÉNÉRATION DU SQUELETTE 3D
# ══════════════════════════════════════════════════════════════════

def open_3d_sketch(swDoc):
    """Ouvre un nouveau sketch 3D — essaie plusieurs méthodes selon version SW."""
    print("    Étape 1 : Insert3DSketch2(False)...")
    try:
        swDoc.Insert3DSketch2(False)
        print("    → OK")
        return
    except TypeError as e:
        print(f"    → TypeError: {e}")

    print("    Étape 2 : Insert3DSketch2() sans argument...")
    try:
        swDoc.Insert3DSketch2()
        print("    → OK")
        return
    except Exception as e:
        print(f"    → Échec: {e}")

    print("    Étape 3 : Insert3DSketch()...")
    try:
        swDoc.Insert3DSketch()
        print("    → OK")
        return
    except Exception as e:
        print(f"    → Échec: {e}")

    raise RuntimeError(
        "Impossible d'ouvrir un sketch 3D via Python.\n"
        "Utilisez le macro VBA : plans/fauteuil_frame.swb\n"
        "Dans SolidWorks : Outils > Macro > Exécuter"
    )


def close_sketch_and_rebuild(swDoc):
    """Ferme le sketch actif et reconstruit le modèle."""
    for method in ["InsertSketch", "Insert3DSketch"]:
        try:
            getattr(swDoc, method)()
            break
        except Exception:
            pass

    for method in ["EditRebuild3", "ForceRebuild3", "EditRebuild"]:
        try:
            fn = getattr(swDoc, method)
            fn(False) if method == "ForceRebuild3" else fn()
            break
        except Exception:
            pass


def build_skeleton(app):
    """Trace tous les axes centraux des tubes dans un sketch 3D."""

    # Utiliser ActiveDoc pour un dispatch plus fiable que le retour de NewDocument
    swDoc = app.ActiveDoc
    if swDoc is None:
        raise RuntimeError("Aucun document actif dans SolidWorks.")

    open_3d_sketch(swDoc)

    sk = swDoc.SketchManager
    if sk is None:
        raise RuntimeError("SketchManager non disponible.")

    print("    Tracé des axes de tubes...")

    # ── Cadres latéraux gauche et droit ─────────────────────────
    for x in (X_L, X_R):

        # 1. Pied arrière complet (sol → siège)
        draw_line(sk, x, Y_REAR, 0,    x, Y_REAR, HS)

        # 2. Rail de siège horizontal (arrière → avant)
        draw_line(sk, x, Y_REAR, HS,   x, Y_FRONT, HS)

        # 3. Pied avant (siège → sol)
        draw_line(sk, x, Y_FRONT, HS,  x, Y_FRONT, 0)

        # 4. Dossier + poignée (depuis jonction siège arrière → poignée)
        draw_line(sk, x, Y_REAR, HS,   x, Y_HANDLE, HH)

        # 5. Accoudoir horizontal
        draw_line(sk, x, Y_ARM_REAR, H_ARMREST,  x, Y_ARM_FRONT, H_ARMREST)

        # 6. Support avant accoudoir (pied avant → accoudoir)
        draw_line(sk, x, Y_ARM_FRONT, HS,        x, Y_ARM_FRONT, H_ARMREST)

        # 7. Support arrière accoudoir (dossier → accoudoir)
        draw_line(sk, x, Y_ARM_REAR,  HS,        x, Y_ARM_REAR,  H_ARMREST)

        # 8. Support repose-pieds (pied avant → repose-pieds)
        draw_line(sk, x, Y_FRONT, H_AXLE_FRONT,  x, Y_FOOTREST, H_FOOTREST)

    # ── Traverses (connexions gauche ↔ droite) ──────────────────

    draw_line(sk, X_L, Y_REAR,     H_AXLE_REAR,  X_R, Y_REAR,     H_AXLE_REAR)   # T1 basse arr
    draw_line(sk, X_L, Y_FRONT,    H_AXLE_FRONT, X_R, Y_FRONT,    H_AXLE_FRONT)  # T2 basse av
    draw_line(sk, X_L, Y_REAR,     HS,           X_R, Y_REAR,     HS)             # T3 siège arr
    draw_line(sk, X_L, Y_FRONT,    HS,           X_R, Y_FRONT,    HS)             # T4 siège av
    draw_line(sk, X_L, Y_HANDLE,   HH,           X_R, Y_HANDLE,   HH)             # T5 poignée
    draw_line(sk, X_L, Y_FOOTREST, H_FOOTREST,   X_R, Y_FOOTREST, H_FOOTREST)    # T6 repose-pieds
    draw_line(sk, X_L, Y_ARM_FRONT, H_ARMREST,   X_R, Y_ARM_FRONT, H_ARMREST)    # T7 accoudoir

    close_sketch_and_rebuild(swDoc)
    print("[OK] Sketch 3D généré — tous les axes de tubes tracés.")


# ══════════════════════════════════════════════════════════════════
#  RÉSUMÉ DES DIMENSIONS
# ══════════════════════════════════════════════════════════════════

def print_summary():
    print()
    print("═" * 50)
    print("  FAUTEUIL DE TRANSFERT — DIMENSIONS v0.1")
    print("═" * 50)
    print(f"  Largeur extérieure   : {W_EXT*1000:.0f} mm")
    print(f"  Largeur intérieure   : {(W_EXT - 0.060 - 0.060)*1000:.0f} mm  (siège)")
    print(f"  Profondeur siège     : {LS*1000:.0f} mm")
    print(f"  Hauteur siège        : {HS*1000:.0f} mm")
    print(f"  Hauteur accoudoir    : {H_ARMREST*1000:.0f} mm")
    print(f"  Hauteur poignée      : {HH*1000:.0f} mm")
    print(f"  Hauteur repose-pieds : {H_FOOTREST*1000:.0f} mm")
    print(f"  Profil tube          : 30 × 30 × 2 mm (acier)")
    print()
    print("  Étape suivante dans SolidWorks :")
    print("  → Pièces soudées > Élément structurel")
    print("  → Standard : ISO  |  Type : Square Tube  |  30x30x2")
    print("═" * 50)


# ══════════════════════════════════════════════════════════════════
#  POINT D'ENTRÉE
# ══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        app  = connect_solidworks()
        new_part(app)           # crée le document — utilise app.ActiveDoc ensuite
        build_skeleton(app)     # passe app pour accéder à ActiveDoc
        print_summary()
    except Exception as e:
        print(f"\n[ERREUR] {e}")
        sys.exit(1)
