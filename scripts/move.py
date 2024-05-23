import os
import shutil

def move_and_rename_annotations(images_dir, annotations_dir):
    for filename in os.listdir(images_dir):
        if filename.endswith('.jpg'):
            basename = os.path.splitext(filename)[0]
            annotation_file = basename + '.txt'
            src = os.path.join(annotations_dir, annotation_file)
            dst = os.path.join(images_dir, annotation_file)
            if os.path.exists(src):
                shutil.copy(src, dst)
            else:
                print(f"Warning: Annotation file {src} does not exist.")

# Déplacer et renommer les annotations d'entraînement
train_images_dir = 'data/GTSRB_Final_Training_Images/Final_Training/Images/preprocessed_jpg'
train_annotations_dir = 'data/GTSRB_Final_Training_Images/Final_Training/Images/annotations'
move_and_rename_annotations(train_images_dir, train_annotations_dir)

# Déplacer et renommer les annotations de test
test_images_dir = 'data/GTSRB_Final_Test_Images/Final_Test/Images/preprocessed_jpg'
test_annotations_dir = 'data/GTSRB_Final_Test_Images/Final_Test/Images/annotations'
move_and_rename_annotations(test_images_dir, test_annotations_dir)