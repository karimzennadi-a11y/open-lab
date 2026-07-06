# Cahier des Charges Fonctionnel
## Fauteuil de transfert médical à domicile
**Version :** 0.1 — Définition du besoin  
**Date :** Juillet 2026  
**Statut :** Brouillon — ouvert à contribution  
**Porteur :** Karim Zennadi — ENP Alger

---

## 1. Présentation générale du problème

### 1.1 Contexte

En Algérie, un nombre croissant de personnes à mobilité réduite (personnes âgées, post-opératoires, handicapées) sont prises en charge à domicile par un aidant familial. Le transfert du patient — du lit vers les toilettes, la salle de bain, ou un fauteuil — représente l'une des tâches les plus physiquement exigeantes et les plus risquées pour l'aidant comme pour le patient.

Les solutions disponibles sur le marché algérien sont soit importées à des prix prohibitifs, soit inadaptées aux contraintes de l'habitat local (couloirs étroits, absence d'ascenseur, sols irréguliers).

### 1.2 Énoncé du besoin — Bête à cornes

```
                    ┌─────────────────────────────────────┐
                    │   À qui rend-il service ?            │
                    │   → L'aidant à domicile              │
                    │   → Le patient à mobilité réduite    │
                    └──────────────┬──────────────────────┘
                                   │
              ┌────────────────────▼────────────────────┐
              │         FAUTEUIL DE TRANSFERT            │
              │            À DOMICILE                    │
              └────────────────────┬────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │   Sur quoi agit-il ?                 │
                    │   → Le patient (corps, confort,      │
                    │     sécurité, dignité)               │
                    └──────────────────────────────────────┘

   Dans quel but ?
   → Faciliter le transfert du patient entre deux positions en toute
     sécurité, avec le minimum d'effort de l'aidant et sans risque
     de chute ou de blessure.
```

### 1.3 Cycle de vie du produit

| Phase | Acteur | Actions |
|-------|--------|---------|
| Fabrication | Atelier national | Soudure, assemblage, finition |
| Livraison / montage | Fournisseur / famille | Transport, montage simple sans outil spécial |
| Utilisation quotidienne | Aidant + patient | Transfert, déplacement, positionnement |
| Nettoyage | Aidant | Essuyage, désinfection |
| Maintenance | Aidant / technicien | Graissage, remplacement roues/sangles |
| Fin de vie | Famille / collecte | Démontage, recyclage acier |

---

## 2. Analyse fonctionnelle — Diagramme pieuvre

```
                            Patient
                               │ FP1
                    FC7        │        FC2
          Aidant ───────── [FAUTEUIL] ─────── Environnement
                               │               (habitat algérien)
                    FC3        │ FC5    FC1
                  Normes    Stockage  Dimensions
                  sécurité             portes/couloirs
                               │
                    FC4        │ FC6    FC8
                  Matériaux   Durée   Coût
                  locaux       de vie  accessible
                               │
                            FC9
                          Entretien
                           simple
```

### Fonctions Principales

| Réf. | Fonction | Critère principal |
|------|----------|-------------------|
| FP1 | Permettre à l'aidant de transférer le patient en toute sécurité | Stabilité, sécurité active |
| FP2 | Assurer le confort et la dignité du patient pendant le transfert | Ergonomie assise, maintien |

### Fonctions Contraintes

| Réf. | Fonction | Critère principal |
|------|----------|-------------------|
| FC1 | S'adapter aux dimensions de l'habitat algérien | Largeur < 65 cm |
| FC2 | Être utilisable par un aidant non professionnel | Simplicité d'usage |
| FC3 | Supporter une charge maximale de 120 kg | Résistance structurelle |
| FC4 | Être fabriqué avec des matériaux disponibles en Algérie | Acier, vinyle, roues industrielles |
| FC5 | Être pliable ou démontable pour le rangement | Encombrement réduit |
| FC6 | Durer plus de 5 ans avec entretien minimal | Durabilité mécanique |
| FC7 | Assurer la stabilité anti-basculement | Anti-tip, empattement suffisant |
| FC8 | Avoir un coût de revient accessible | < 50 000 DZD (cible) |
| FC9 | Permettre le nettoyage et la désinfection | Matériaux lavables |

---

## 3. Cahier des charges fonctionnel — Tableau CdCF

| Réf. | Fonction | Critère d'évaluation | Niveau | Flexibilité |
|------|----------|----------------------|--------|-------------|
| FP1 | Transfert sécurisé | Charge maximale statique | 120 kg | F0 — non négociable |
| FP1 | Transfert sécurisé | Charge maximale dynamique (choc) | 150 kg | F0 |
| FP1 | Transfert sécurisé | Angle d'inclinaison max sans basculement | > 10° | F1 |
| FP2 | Confort patient | Hauteur d'assise réglable | 45 – 55 cm | F1 |
| FP2 | Confort patient | Largeur d'assise | 45 cm min | F1 |
| FP2 | Confort patient | Accoudoirs escamotables (transfert latéral) | Oui | F0 |
| FP2 | Confort patient | Repose-pieds escamotables | Oui | F1 |
| FC1 | Dimensions habitat | Largeur hors-tout | ≤ 65 cm | F0 |
| FC1 | Dimensions habitat | Longueur hors-tout | ≤ 115 cm | F2 |
| FC1 | Dimensions habitat | Rayon de braquage | ≤ 80 cm | F1 |
| FC2 | Facilité d'usage | Effort de poussée sur sol plat | ≤ 25 N | F1 |
| FC2 | Facilité d'usage | Temps d'apprentissage aidant | < 30 min | F2 |
| FC4 | Matériaux locaux | Acier tubulaire (EN 10219 ou équiv.) | Standard Algérie | F0 |
| FC4 | Matériaux locaux | Revêtement assise | Vinyle lavable | F1 |
| FC5 | Pliabilité | Dimensions plié (L×l×h) | ≤ 120×35×90 cm | F2 |
| FC5 | Pliabilité | Temps pliage/dépliage | < 30 secondes | F2 |
| FC6 | Durabilité | Durée de vie minimale | 5 ans / 10 000 transferts | F1 |
| FC6 | Durabilité | Protection anticorrosion | Peinture époxy ou galvanisation | F1 |
| FC7 | Stabilité | Charge de basculement latéral | > 200 N à 30 cm du centre | F0 |
| FC7 | Stabilité | Freins roues arrière | Présents et verrouillables | F0 |
| FC8 | Coût | Coût de revient fabrication | < 50 000 DZD | F2 |
| FC9 | Nettoyage | Résistance aux désinfectants courants | Oui | F0 |
| FC9 | Nettoyage | Absence de zones de rétention | Conception lisse | F1 |

**Flexibilité :**  
- F0 = Impératif — aucune dérogation possible  
- F1 = Souhaitable — dérogation acceptée si justifiée  
- F2 = Indicatif — objectif à atteindre en V1  

---

## 4. Contraintes réglementaires et normatives

| Domaine | Norme / Référence | Remarque |
|---------|------------------|---------|
| Fauteuils roulants médicaux | ISO 7176-1 à 7176-26 | Référence internationale — à adapter au contexte local |
| Résistance structurelle | ISO 7176-8 | Tests de charge statique et dynamique |
| Stabilité | ISO 7176-1 | Tests d'inclinaison |
| Dispositifs médicaux (Algérie) | Décret 90-35 + réglementation INAPI | Dispositif médical classe I |
| Sécurité électrique | Non applicable (produit 100% mécanique) | — |

---

## 5. Données d'entrée techniques

### Dimensions de référence — Habitat algérien

| Élément | Dimension typique |
|---------|------------------|
| Largeur de porte standard | 80 – 90 cm (passage utile ≈ 70 – 75 cm) |
| Largeur couloir appartement | 80 – 100 cm |
| Hauteur lit à domicile | 50 – 70 cm |
| Hauteur toilettes | 40 – 45 cm |
| Hauteur fauteuil standard | 45 – 50 cm |

### Profil utilisateur

| Utilisateur | Caractéristiques |
|-------------|-----------------|
| Patient | Mobilité réduite, masse ≤ 120 kg, nécessite aide pour se lever/s'asseoir |
| Aidant | Membre de la famille, sans formation paramédicale, force physique variable |

### Matériaux cibles (disponibilité nationale)

| Composant | Matériau | Disponibilité |
|-----------|----------|--------------|
| Châssis | Tube acier carré 30×30×2 mm | Bonne — profilés standard |
| Assise / dossier | Mousse haute densité + vinyle | Bonne — industrie locale |
| Roues | Roues industrielles Ø 200 mm (pivotantes + fixes) | Bonne — fournisseurs locaux |
| Freins | Frein à pied sur roues arrière | Bonne |
| Finition | Peinture époxy ou poudre | Bonne |

---

## 6. Solutions à explorer (pistes de conception)

- [ ] Châssis tubulaire soudé pliant en X (type civière pliante)
- [ ] Accoudoirs à rotation vers l'arrière (transfert latéral facilité)
- [ ] Hauteur d'assise fixe v0.1 / réglable par trous et goupille v1.0
- [ ] Repose-pieds escamotable par rotation
- [ ] Poignées de poussée en tube coudé soudé
- [ ] Sangles de maintien latéral (option)

---

## 7. Critères de validation

Le prototype v0.1 sera validé si :

1. Il supporte 120 kg en usage statique sans déformation permanente
2. Il passe dans une ouverture de 70 cm (porte standard)
3. Un aidant adulte peut le pousser sur sol plat avec un effort ≤ 25 N
4. Il ne bascule pas sous un effort latéral de 200 N appliqué à 30 cm au-dessus du siège
5. Il se plie en moins de 30 secondes
6. L'assise est nettoyable avec un désinfectant standard

---

## 8. Jalons du projet

| Phase | Livrable | Statut |
|-------|----------|--------|
| 1 — Besoin | Cahier des charges v0.1 | En cours |
| 2 — Conception | Plans CAO, dessins de définition | — |
| 3 — Calculs | Vérification résistance châssis | — |
| 4 — Prototype | Maquette bois ou prototype acier | — |
| 5 — Validation | Tests de charge et stabilité | — |
| 6 — Business plan | Analyse coût, marché, distribution | — |

---

## Contributeurs

| Nom | Compétence | Contribution |
|-----|-----------|-------------|
| Karim Zennadi | Ingénierie mécanique | Rédaction initiale du CdCF |

*Pour contribuer : ouvrir une Issue sur GitHub ou contacter karimzennadi@gmail.com*

---

*Open Lab — ENP Alger · Licence MIT · v0.1 · Juillet 2026*
