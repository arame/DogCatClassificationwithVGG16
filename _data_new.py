import os, shutil, glob
from sklearn.model_selection import train_test_split
from PIL import Image

def remove_corrupt_images(image_paths):
    j = 0
    for i, img_path in enumerate(image_paths):
        try:
            img = Image.open(img_path)
        except:
            print(f"Invalid image {i} {img_path} removed") 
            image_paths.remove(img_path)
            j += 1
            
    print(f"{j} images removed")
    
    return image_paths

def create_folder(folder):
    if os.path.exists(folder) == False:
        os.makedirs(folder)

def copy_type(type, image_folder, train_folder, val_folder, test_folder):
    file_path = os.path.join(image_folder,f'{type}*.jpg')
    image_paths = glob.glob(file_path)
    image_paths = remove_corrupt_images(image_paths)
    train, val = train_test_split(image_paths, test_size=0.25, random_state=42, shuffle=True)
    val, test = train_test_split(val, test_size=0.20, random_state=42, shuffle=True)
    for image in train:
        shutil.copy(image, train_folder)
    for image in val:
        shutil.copy(image, val_folder)
    for image in test:
        shutil.copy(image, test_folder)

def organise_images_in_folders(image_folder, classes):
    _train_folder = os.path.join(image_folder, "data", "train")
    if os.path.exists(_train_folder):
        print("Folder exists for training images, no need to organise data")
        return
    _val_folder = os.path.join(image_folder, "data", "val")
    _test_folder = os.path.join(image_folder, "data", "test")
    for cls in classes:
        train_folder = os.path.join(_train_folder, cls)
        create_folder(train_folder)
        val_folder = os.path.join(_val_folder, cls)
        create_folder(val_folder)
        test_folder = os.path.join(_test_folder, cls)
        create_folder(test_folder)
        copy_type(cls, image_folder, train_folder, val_folder, test_folder)



