import os
from PIL import Image

folder_path = './saved_images/org'
left_folder_path = './saved_images/left'
right_folder_path = './saved_images/right'

# Create left and right folders if they don't exist
os.makedirs(left_folder_path, exist_ok=True)
os.makedirs(right_folder_path, exist_ok=True)

image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for file_name in image_files:
    image = Image.open(os.path.join(folder_path, file_name))

    width = image.width

    left_half = image.crop((0, 0, width // 2, image.height))
    right_half = image.crop((width // 2, 0, width, image.height))

    file_extension = os.path.splitext(file_name)[1]

    left_file_name = f"{os.path.splitext(file_name)[0]}.l{file_extension}"
    right_file_name = f"{os.path.splitext(file_name)[0]}.r{file_extension}"

    left_half.save(os.path.join(left_folder_path, left_file_name))
    right_half.save(os.path.join(right_folder_path, right_file_name))