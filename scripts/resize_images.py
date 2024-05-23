import pandas as pd
import os
from PIL import Image

# Chemins vers les fichiers et répertoires
base_path = '/Users/tarekatbi/Desktop/ML/env/data/GTSRB_Final_Training_Images/Final_Training/Images'
output_base_dir = '/Users/tarekatbi/Desktop/ML/env/data/GTSRB_Preprocessed'
img_size = (416, 416)  # Taille à laquelle redimensionner les images

# Liste des répertoires de classes (43 au total)
class_dirs = [f"{i:05d}" for i in range(43)]

# Créer le répertoire de sortie s'il n'existe pas
os.makedirs(output_base_dir, exist_ok=True)

def preprocess_class(class_dir):
    csv_path = os.path.join(base_path, class_dir, f'GT-{class_dir}.csv')
    output_class_dir = os.path.join(output_base_dir, class_dir)
    os.makedirs(output_class_dir, exist_ok=True)

    if os.path.exists(csv_path):
        # Lire le fichier CSV
        df = pd.read_csv(csv_path, sep=';')
        print(f"Traitement du fichier {csv_path} avec {len(df)} images...")
        for index, row in df.iterrows():
            filename = row['Filename']
            class_id = row['ClassId']
            x1, y1, x2, y2 = row['Roi.X1'], row['Roi.Y1'], row['Roi.X2'], row['Roi.Y2']

            # Lire l'image
            img_path = os.path.join(base_path, class_dir, filename)
            if not os.path.exists(img_path):
                print(f"Image manquante: {img_path}")
                continue

            image = Image.open(img_path)

            # Découper l'image
            cropped_image = image.crop((x1, y1, x2, y2))

            # Redimensionner l'image
            resized_image = cropped_image.resize(img_size, Image.ANTIALIAS)
            
            # Enregistrer l'image prétraitée
            output_img_path = os.path.join(output_class_dir, f"{filename.split('.')[0]}.jpg")
            resized_image.save(output_img_path)

            # Créer un fichier d'annotation correspondant
            annotation_path = os.path.join(output_class_dir, f"{filename.split('.')[0]}.txt")
            width, height = row['Width'], row['Height']
            with open(annotation_path, 'w') as f:
                f.write(f"{class_id} {(x1 + x2) / 2 / width} {(y1 + y2) / 2 / height} {(x2 - x1) / width} {(y2 - y1) / height}")

        print(f"Traitement terminé pour {csv_path}. Total d'images traitées : {len(df)}")
    else:
        print(f"CSV manquant pour la classe {class_dir}")

# Exécuter le prétraitement pour chaque classe
for class_dir in class_dirs:
    preprocess_class(class_dir)

print(f"Prétraitement terminé. Les images ont été redimensionnées à {img_size[0]}x{img_size[1]} pixels.")
