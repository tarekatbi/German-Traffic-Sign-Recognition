# Détection Automatique des Panneaux de Signalisation

## Description
Ce projet utilise le modèle YOLOv5 pour détecter automatiquement les panneaux de signalisation à partir d'images et de vidéos. L'application est développée avec Streamlit pour offrir une interface utilisateur interactive, permettant de télécharger des fichiers et de visualiser les résultats de détection en temps réel.

## Contenu du Projet
- **app/** : Contient le code source de l'application Streamlit.
- **data/** : Dossier contenant les ensembles de données d'entraînement et de test.
- **models/** : Dossier contenant les configurations du modèle YOLOv5.
- **requirements.txt** : Liste des dépendances nécessaires pour exécuter le projet.
- **scripts/** : Scripts pour le prétraitement des données et l'entraînement du modèle.
- **Dockerfile** : Fichier pour la containerisation de l'application avec Docker.

## Prérequis
- Python 3.x
- pip (Python package installer)
- Git

## Installation

### 1. Cloner le Répertoire
```bash
git clone https://github.com/tarekatbiGerman-Traffic-Sign-Recognition.git
cd votre-depot
```

### 2. Cloner le Modèle YOLOv5
```bash
git clone https://github.com/ultralytics/yolov5.git
```

### 3. Copier le Fichier YAML
Copiez le fichier gtsrb.yaml qui se trouve dans le dossier models vers le répertoire yolov5/data.
```bash
cp model/gtsrb.yaml yolov5/data/
```
### 4. Créer un Environnement Virtuel
```bash
python -m venv env
source env/bin/activate  # Sur macOS/Linux
.\env\Scripts\activate   # Sur Windows

```
### 5. Installer les Dépendances
```bash
pip install -r requirements.txt
```
## Prétraitement des Données
Avant d'entraîner le modèle, les données doivent être prétraitées. Utilisez le script de prétraitement pour convertir et redimensionner les images, ainsi que pour créer les annotations nécessaires.
### Commande pour Prétraiter les Données
```bash
python scripts/preprocess.py
```
## Entraînement du Modèle
Utilisez le script d'entraînement pour entraîner le modèle YOLOv5 sur les données prétraitées.

### Commande pour Entraîner le Modèle
```bash
python train.py --img 640 --batch 32 --epochs 50 --data data/gtsrb.yaml --cfg models/yolov5s.yaml --weights yolov5s.pt --patience 10
```
### Note
L'entraînement prend environ 2 heures par époque. Vous pouvez ajuster les hyperparamètres selon vos besoins. L'entraînement peut être interrompu manuellement si les métriques de performance sont satisfaisantes avant la fin des 50 époques.

## Déploiement de l'Application
L'application Streamlit permet d'interagir avec le modèle et de visualiser les résultats de détection. Vous pouvez déployer l'application localement ou en utilisant Docker.

### Exécution Locale
```bash
streamlit run app/app.py
```
## Contribution
Les contributions sont les bienvenues. Veuillez soumettre des pull requests ou ouvrir des issues pour discuter des modifications que vous souhaitez apporter.