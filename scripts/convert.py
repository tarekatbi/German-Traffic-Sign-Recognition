import os
import cv2

def convert_images(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.endswith('.ppm'):
            # Read the image
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path)

            # Convert and save as .jpg
            new_filename = os.path.splitext(filename)[0] + '.jpg'
            new_img_path = os.path.join(output_dir, new_filename)
            cv2.imwrite(new_img_path, img)

# Convert training images
train_input_dir = 'data/GTSRB_Final_Training_Images/Final_Training/Images/preprocessed'
train_output_dir = 'data/GTSRB_Final_Training_Images/Final_Training/Images/preprocessed_jpg'
convert_images(train_input_dir, train_output_dir)

# Convert test images
test_input_dir = 'data/GTSRB_Final_Test_Images/Final_Test/Images/preprocessed'
test_output_dir = 'data/GTSRB_Final_Test_Images/Final_Test/Images/preprocessed_jpg'
convert_images(test_input_dir, test_output_dir)