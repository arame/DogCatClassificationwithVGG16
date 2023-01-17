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

def organise_images_in_folders():
    image_folder = "car_flower_small"
    train_folder = os.path.join(image_folder, "data", "trainset")
    if os.path.exists(train_folder):
        print("Folder exists for training images, no need to organise data")
        return
    car_train_folder = os.path.join(train_folder, "car")
    create_folder(car_train_folder)
    flower_train_folder = os.path.join(train_folder, "flower")
    create_folder(flower_train_folder)
    test_folder = os.path.join(image_folder, "data", "testset")
    car_test_folder = os.path.join(test_folder, "car")
    create_folder(car_test_folder)
    flower_test_folder = os.path.join(test_folder, "flower")
    create_folder(flower_test_folder)

    copy_type("car", image_folder, car_train_folder, car_test_folder)
    copy_type("flower", image_folder, flower_train_folder, flower_test_folder)


