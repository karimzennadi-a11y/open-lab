# Dimensions du cadre — Fauteuil de transfert v0.1

## Profil tube
**Acier carré : 30 × 30 × 2 mm** (EN 10219 ou équivalent national)

---

## Vue de côté (plan XZ, X = axe longitudinal, Z = vertical)

```
Z (mm)
950 ──  ●════════════════════════════════════● ← Poignée (traverse T5)
        ║                                    ║
        ║  dossier incliné                   ║
        ║  (légèrement vers l'arrière)       ║
730 ──  ●══════════════════════════════════● ← Accoudoir (traverse T7)
        ║                                  ║
500 ──  ●══════════════════════════════════● ← Siège (traverses T3, T4)
        ║  Rail de siège horizontal 420mm   ║
        ║                                  ║
100 ──  ●                                  ● ← Axle roues (T1, T2)
        ║                                  ║
  0 ──  ●══════════════════════════════════● ← Sol
       Arr.    ←── 420 mm ──→           Av.

       ← 50mm →←──── 420 mm ────→← 100 mm →
       (handle)   (profondeur siège)  (repose-pieds)
```

---

## Vue de face (plan YZ, Y = largeur, Z = vertical)

```
Z (mm)
950 ──  ●══════════════════════════════════● ← Poignée
        ║                                  ║
730 ──  ●══════════════════════════════════● ← Accoudoir
        ║                                  ║
500 ──  ●══════════════════════════════════● ← Siège
        ║                                  ║
100 ──  ●                                  ● ← Axle roue
        ║                                  ║
  0 ──  ●══════════════════════════════════● ← Sol

        ←──────── 620 mm ──────────────────→  (hors-tout)
           30      ←── 500 mm ──→       30    (tube + siège + tube)
```

---

## Tableau récapitulatif des cotes

| Élément | Cote | Valeur |
|---------|------|--------|
| Largeur hors-tout | W_ext | **620 mm** |
| Largeur intérieure (siège) | W_int | **500 mm** |
| Profondeur siège | Ls | **420 mm** |
| Hauteur siège | Hs | **500 mm** |
| Hauteur accoudoir | Ha | **730 mm** |
| Hauteur poignée | Hh | **950 mm** |
| Hauteur repose-pieds | Hf | **80 mm** |
| Hauteur axle roue arrière | Hr_r | **100 mm** (roue Ø200mm) |
| Hauteur axle roue avant | Hr_f | **75 mm** (roue Ø150mm) |
| Position repose-pieds | Y_rf | **520 mm** depuis arrière |
| Recul poignée / axle arrière | ΔY_h | **50 mm** en arrière |

---

## Éléments structurels (tubes)

| Réf. | Désignation | De | À |
|------|-------------|-----|---|
| C1 | Cadre gauche — pied arrière | (−310, 0, 0) | (−310, 0, 500) |
| C2 | Cadre gauche — rail siège | (−310, 0, 500) | (−310, 420, 500) |
| C3 | Cadre gauche — pied avant | (−310, 420, 500) | (−310, 420, 0) |
| C4 | Cadre gauche — dossier + poignée | (−310, 0, 500) | (−310, −50, 950) |
| C5 | Cadre gauche — accoudoir | (−310, 20, 730) | (−310, 370, 730) |
| C6 | Cadre gauche — support accoudoir av. | (−310, 370, 500) | (−310, 370, 730) |
| C7 | Cadre gauche — support accoudoir arr. | (−310, 20, 500) | (−310, 20, 730) |
| C8 | Cadre gauche — support repose-pieds | (−310, 420, 75) | (−310, 520, 80) |
| D1…D8 | Cadre droit (symétrique X → +310) | *idem* | *idem* |
| T1 | Traverse basse arrière | (−310, 0, 100) | (+310, 0, 100) |
| T2 | Traverse basse avant | (−310, 420, 75) | (+310, 420, 75) |
| T3 | Traverse siège arrière | (−310, 0, 500) | (+310, 0, 500) |
| T4 | Traverse siège avant | (−310, 420, 500) | (+310, 420, 500) |
| T5 | Traverse poignée | (−310, −50, 950) | (+310, −50, 950) |
| T6 | Traverse repose-pieds | (−310, 520, 80) | (+310, 520, 80) |
| T7 | Traverse accoudoir | (−310, 370, 730) | (+310, 370, 730) |

*Coordonnées en mm — Origine : centre axle arrière au sol*

---

## Étapes de modélisation SolidWorks

1. **Exécuter le script** `generate_frame_3d.py` → sketch 3D généré automatiquement
2. **Pièces soudées** → Élément structurel → ISO → Square Tube → 30x30x2
   - Sélectionner chaque groupe de lignes colinéaires
3. **Coupes d'onglet** pour les jonctions tubes
4. **Symétrie** : modéliser le cadre gauche, miroir sur plan XZ pour le cadre droit
5. **Roues** : insérer comme composants dans l'assemblage (modèles standards)
6. **Simulation** : appliquer charge 1200 N (120 kg × g) sur rail de siège

---

*Open Lab — ENP Alger · v0.1 · Juillet 2026*
