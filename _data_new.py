import os, shutil
from sklearn.model_selection import train_test_split
import glob

def create_folder(folder):
    if os.path.exists(folder) == False:
        os.makedirs(folder)

def copy_type(type, image_folder, train_folder, test_folder):
    file_path = os.path.join(image_folder,f'{type}*.jpg')
    image_paths = glob.glob(file_path)
    train, test = train_test_split(image_paths, test_size=0.25, random_state=42, shuffle=True)
    for image in train:
        shutil.copy(image, train_folder)
    for image in test:
        shutil.copy(image, test_folder)

def organise_images_in_folders(image_folder, classes):
    _train_folder = os.path.join(image_folder, "data", "train")
    if os.path.exists(_train_folder):
        print("Folder exists for training images, no need to organise data")
        return
    _test_folder = os.path.join(image_folder, "data", "test")
    for cls in classes:
        train_folder = os.path.join(_train_folder, cls)
        create_folder(train_folder)
        test_folder = os.path.join(_test_folder, cls)
        create_folder(test_folder)
        copy_type(cls, image_folder, train_folder, test_folder)



