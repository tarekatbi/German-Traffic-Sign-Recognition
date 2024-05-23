import os

# Chemin vers le répertoire contenant les images prétraitées
preprocessed_jpg_path = '/Users/tarekatbi/Desktop/ML/env/data/GTSRB_Final_Training_Images/Final_Training/Images/preprocessed_jpg'

# Obtenir la liste de tous les fichiers dans le répertoire
all_files = os.listdir(preprocessed_jpg_path)

# Filtrer uniquement les fichiers .jpg
jpg_files = [file for file in all_files if file.endswith('.jpg')]

# Compter le nombre de fichiers .jpg
num_jpg_files = len(jpg_files)
print(f"Nombre de fichiers .jpg dans le répertoire : {num_jpg_files}")