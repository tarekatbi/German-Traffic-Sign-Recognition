import os

def update_annotations(image_dir, annotation_dir):
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg'):
            basename = os.path.splitext(filename)[0]
            annotation_file = basename + '.txt'
            annotation_path = os.path.join(annotation_dir, annotation_file)
            if os.path.exists(annotation_path):
                with open(annotation_path, 'r') as file:
                    content = file.read()

                # Rewrite the same annotation file to ensure it's linked to the new image
                with open(annotation_path, 'w') as file:
                    file.write(content)
            else:
                print(f"Warning: Annotation file {annotation_path} does not exist.")

# Update training annotations
train_image_dir = 'data/GTSRB_Final_Training_Images/Final_Training/Images/preprocessed_jpg'
train_annotation_dir = 'data/GTSRB_Final_Training_Images/Final_Training/Images/annotations'
update_annotations(train_image_dir, train_annotation_dir)

# Update test annotations
test_image_dir = 'data/GTSRB_Final_Test_Images/Final_Test/Images/preprocessed_jpg'
test_annotation_dir = 'data/GTSRB_Final_Test_Images/Final_Test/Images/annotations'
update_annotations(test_image_dir, test_annotation_dir)