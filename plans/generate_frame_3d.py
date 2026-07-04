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


def new_part(app):
    """Crée un nouveau document Part."""
    template = app.GetUserPreferenceStringValue(9)  # Chemin template part
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

def build_skeleton(doc):
    """Trace tous les axes centraux des tubes dans un sketch 3D."""

    doc.Insert3DSketch2(True)        # Ouvre le sketch 3D
    sk = doc.SketchManager

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

    # T1 — Traverse basse arrière (au niveau axle roue arrière)
    draw_line(sk, X_L, Y_REAR,    H_AXLE_REAR,  X_R, Y_REAR,    H_AXLE_REAR)

    # T2 — Traverse basse avant (au niveau axle roue avant)
    draw_line(sk, X_L, Y_FRONT,   H_AXLE_FRONT, X_R, Y_FRONT,   H_AXLE_FRONT)

    # T3 — Traverse siège arrière
    draw_line(sk, X_L, Y_REAR,    HS,            X_R, Y_REAR,    HS)

    # T4 — Traverse siège avant
    draw_line(sk, X_L, Y_FRONT,   HS,            X_R, Y_FRONT,   HS)

    # T5 — Traverse poignée
    draw_line(sk, X_L, Y_HANDLE,  HH,            X_R, Y_HANDLE,  HH)

    # T6 — Traverse repose-pieds
    draw_line(sk, X_L, Y_FOOTREST, H_FOOTREST,   X_R, Y_FOOTREST, H_FOOTREST)

    # T7 — Traverse accoudoir avant (optionnelle — maintien latéral)
    draw_line(sk, X_L, Y_ARM_FRONT, H_ARMREST,   X_R, Y_ARM_FRONT, H_ARMREST)

    doc.Insert3DSketch2(False)      # Ferme le sketch 3D
    doc.EditRebuild3()
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
        doc  = new_part(app)
        build_skeleton(doc)
        print_summary()
    except Exception as e:
        print(f"\n[ERREUR] {e}")
        sys.exit(1)
