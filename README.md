# video-resize (ddtm62)

Ce dépot contient des scripts python qui configure Avidemux pour redimensionner des vidéos (sous Windows).

## Instalation

Les fichiers `.py` presents dans se dépots sont à mettre dans le dossier `C:\Users\<Utilisateur>\AppData\Roaming\avidemux\custom` où `<Utilisateur>` est à remplacer par le nom de l'utilisateur Windows. Pour accèder au dossier `C:\Users\<Utilisateur>\AppData\Roaming\avidemux` on peut utiliser le menu **Aide » Avancé » Ovrir le dossier de l'application**.

Une fois ces fichiers copiés dans le dossier `custom`, après redémagarage de Avidemux, dans le menu **Scripts perso** deux nouveaux sous menus doivent être présents :
- **Redimensionner exactement 720x480 (avec coupe)** - pour redimensionner la video en `720 × 480` avec découpe éventuelle si le rapport n'est pas 2:3.
- **Redimensionner au plus 720x480** - pour redimensionner la video en `720 × H`, avec `H ≤ 480`, ou en `W × 480`, avec `W ≤ 720`.

## Utilisation

1. Ouvrir la vidéo
1. Selectionner l'un des deux ménus.
1. Sauver la vidéo (sous un autre noms). L'encodage démare et prends un certain temps.
