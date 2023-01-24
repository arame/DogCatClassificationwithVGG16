from PIL import Image
import glob, os, random

def get_data(data_folder):
    file_path = os.path.join(data_folder, "data", "train", "*\\*")
    list = glob.glob(file_path)
    X_list = random.sample(list, len(list))
    return X_list

def main():
    X = get_data("cats_dogs_small")
    for i, img_path in enumerate(X):
        try:
            img = Image.open(img_path)
        except:
            print(f"Invalid image {i} {img_path} removed") 
            os.remove(img_path)
              

if __name__ == "__main__":
    main()