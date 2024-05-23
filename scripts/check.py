import os

def check_files(directory):
    images = [f for f in os.listdir(directory) if f.endswith('.jpg')]
    annotations = [f for f in os.listdir(directory) if f.endswith('.txt')]

    print(f"Found {len(images)} images and {len(annotations)} annotations in {directory}")
    for img in images:
        base_name = os.path.splitext(img)[0]
        annotation_file = base_name + '.txt'
        if annotation_file not in annotations:
            print(f"Missing annotation for image: {img}")
            return False
    return True

train_dir = 'data/GTSRB_Final_Training_Images/Final_Training/Images/preprocessed_jpg'
val_dir = 'data/GTSRB_Final_Test_Images/Final_Test/Images/preprocessed_jpg'

train_check = check_files(train_dir)
val_check = check_files(val_dir)

if not train_check:
    print("There are missing annotations in the training directory.")
if not val_check:
    print("There are missing annotations in the validation directory.")