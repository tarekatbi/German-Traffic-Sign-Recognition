import os

def check_and_fix_annotations(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            valid_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 5:
                    class_id = int(parts[0])
                    if class_id == -1:
                        print(f"Invalid class ID found in {filename}. Correcting it.")
                        # Here you should replace -1 with a valid class id
                        parts[0] = '0'  # Assuming 0 is a valid class ID for testing
                    valid_lines.append(' '.join(parts))
            
            # Rewrite the corrected annotations back to the file
            with open(file_path, 'w') as file:
                for line in valid_lines:
                    file.write(f"{line}\n")

# Check and fix training annotations
train_annotation_dir = 'data/GTSRB_Final_Training_Images/Final_Training/Images/preprocessed_jpg'
check_and_fix_annotations(train_annotation_dir)

# Check and fix test annotations
test_annotation_dir = 'data/GTSRB_Final_Test_Images/Final_Test/Images/preprocessed_jpg'
check_and_fix_annotations(test_annotation_dir)