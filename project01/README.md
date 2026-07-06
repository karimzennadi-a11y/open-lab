# Projet 01 — Fauteuil de transfert médical

> Dispositif d'assistance à la mobilité pour personnes à mobilité réduite  
> Fabrication nationale · Open Source · ENP Alger — Open Lab

---

## Objectif

Concevoir un fauteuil de transfert médical adapté au contexte algérien :
- Transfert lit ↔ fauteuil roulant, chambre ↔ sanitaires
- Structure tubulaire acier 30×30 mm, siège réglable 40–60 cm
- Accoudoirs relevables, repose-pieds escamotable, 4 roulettes avec freins
- Capacité : 120 kg
- Fabricable localement avec des matériaux accessibles

## Statut actuel

| Phase | État |
|-------|------|
| 01 · Idée & analyse du besoin | ✅ Terminé |
| 02 · Cahier des charges | ✅ v0.1 rédigé |
| 03 · Conception CAO | 🔄 En cours — squelette 3D SolidWorks |
| 04 · Prototype | ⏳ À venir |
| 05 · Business Plan | ⏳ À venir |

## Structure du répertoire

```
project01/
├── docs/
│   └── CDC_fauteuil_transfert_v0.1.md   # Cahier des charges complet
├── plans/
│   ├── croquis_cadre_v0.1.svg           # Vue de côté cotée
│   ├── croquis_3d_manquants.svg         # Éléments manquants en vue iso
│   ├── DIMENSIONS_cadre_v0.1.md         # Tableau des dimensions
│   ├── fauteuil_frame.bas               # Macro VBA SolidWorks
│   └── generate_frame_3d.py             # Script Python (API SolidWorks)
├── images/                              # Photos de référence (à venir)
└── fabrication/                         # Calculs, matériaux, fournisseurs (à venir)
```

## Comment contribuer

Toute compétence est bienvenue — ingénieur mécanique, médecin, ergonome, fabricant, économiste.

1. Lire le [cahier des charges](docs/CDC_fauteuil_transfert_v0.1.md)
2. Ouvrir une **Issue** sur GitHub pour proposer une amélioration ou signaler un problème
3. Forker le repo, faire vos modifications, soumettre une **Pull Request**
4. Ou simplement écrire à [karimzennadi@gmail.com](mailto:karimzennadi@gmail.com)

Voir [CONTRIBUTING.md](../CONTRIBUTING.md) pour les détails.

## Lancer la CAO (SolidWorks)

**Via macro VBA :**
1. Ouvrir SolidWorks, créer un nouveau Part
2. `Outils > Macro > Nouveau` → coller le contenu de `plans/fauteuil_frame.bas`
3. Exécuter avec **F5**

**Via script Python :**
```bash
conda activate env_these
python plans/generate_frame_3d.py
```
Puis dans SolidWorks : `Pièces soudées > Élément structurel > ISO > Square Tube > 30×30×2.6`

## Dimensions clés

| Paramètre | Valeur |
|-----------|--------|
| Largeur extérieure | 620 mm |
| Profondeur siège | 420 mm |
| Hauteur siège | 500 mm |
| Hauteur accoudoir | 730 mm |
| Hauteur poignée | 950 mm |
| Profil tube | 30 × 30 × 2 mm acier |
| Capacité | 120 kg |

## Porteur de projet

**Karim Zennadi** — ENP Alger  
[karimzennadi@gmail.com](mailto:karimzennadi@gmail.com) · [LinkedIn](https://www.linkedin.com/in/karim-zennadi-24579276/)

---

*Open Lab · Conception Produit · Alger · 2026*
