# video-resize (ddtm62)

[Ce dépôt](https://github.com/ddtm62/video-resize) contient des scripts python qui configure Avidemux pour redimensionner des vidéos (sous Windows).

## Installation

Les fichiers deux `.py` présents dans ce dépôts

- [Redimensionner au plus 720x480.py](https://ddtm62.github.io/video-resize/Redimensionner%20au%20plus%20720x480.py)
- [Redimensionner exactement 720x480 (avec coupe).py](https://ddtm62.github.io/video-resize/Redimensionner%20exactement%20720x480%20%28avec%20coupe%29.py)

sont à mettre dans le dossier `C:\Users\<Utilisateur>\AppData\Roaming\avidemux\custom`, où `<Utilisateur>` est à remplacer par le nom de l'utilisateur Windows.

_(Pour accéder au dossier `C:\Users\<Utilisateur>\AppData\Roaming\avidemux` on peut éventuellement utiliser le menu **Aide » Avancé » Ouvrir le dossier de l'application** de Avidemux.)_

Une fois ces fichiers copiés dans le dossier `custom`, après redémarrage de Avidemux, dans le menu **Scripts perso** deux nouveaux sous menus doivent être présents :
- **Redimensionner exactement 720x480 (avec coupe)** - pour redimensionner la vidéo en `720 × 480` avec découpe éventuelle si le rapport n'est pas 2:3.
- **Redimensionner au plus 720x480** - pour redimensionner la vidéo en `720 × H`, avec `H ≤ 480`, ou en `W × 480`, avec `W ≤ 720`.

## Utilisation

1. Ouvrir la vidéo
1. Sélectionner l'un des deux menus.
1. Sauver la vidéo (sous un autre noms). L'encodage démarre et prends un certain temps.
