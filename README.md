# Space_photos_sender (Expéditeur d'images spatiales)

## Le programme envoie les dernières photos de SpaceX à un canal Telegram si elles sont disponibles, sinon il envoie une image par défaut.

## Fonctionnalités principales

- Récupération des données des derniers lancements de SpaceX via leur API.
- Téléchargement des images associées aux lancements.
- Publication automatique des images sur un canal Telegram.
- Prise en charge des commandes pour la publication manuelle de messages et d'images.

## Étapes de lancement du programme :
1) Clonez le projet :
```bash
git clone https://github.com/alisaaaf/Space-images-sender.git 
```
2) Pour installer toutes les bibliothèques nécessaires, ouvrez un terminal dans le dossier du projet téléchargé et exécutez la commande suivante :
```bash
pip install -r requirements.txt
```
3) Créez un fichier .env à la racine du projet et ajoutez les variables suivantes :
```plaintext
TOKEN=votre_token_bot
```
Vous pouvez obtenir un token en créant un bot sur [BotFather](https://t.me/botfather).

4) Exécutez le fichier message_sender.py avec la commande suivante dans le terminal du projet :
```bash
python message_sender.py
```
5) Commandes du bot :

- /start — commande de test, répond avec le même texte que celui saisi.
- /publish_text — publie un message texte de test dans le canal Telegram spécifié.
- /publish_photo — télécharge les images via l'API SpaceX et les publie dans le canal Telegram.

6) Par défaut, la publication est programmée à 07:00. Si vous souhaitez modifier l'heure, éditez la ligne suivante : 
**schedule.every().day.at("00:00").do(publish_photo)** à la fin du fichier **message_sender**.

## Remarques

1. Assurez-vous que le bot est ajouté à votre canal en tant qu'administrateur pour qu'il puisse publier des messages.
2. Si l'API SpaceX ne fournit pas de liens vers des images, le script effectue une requête vers un lancement de secours.
