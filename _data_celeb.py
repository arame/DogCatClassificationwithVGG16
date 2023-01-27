import os, shutil

def organise_images_in_folders(df_celeb, gl, image_folder, data_folder):
    data1_folder = os.path.join(data_folder, "data")
    if os.path.exists(data1_folder):
        print("folders for male and female already exist")
        return
    
    male_folder = os.path.join(data1_folder, "male")
    os.makedirs(male_folder)
    
    female_folder = os.path.join(data1_folder, "female")
    os.makedirs(female_folder)
    print("male and female folders created")
    
    df_celeb_image = df_celeb[gl.image_id].copy()
    df_gender = df_celeb[gl.is_male].copy()
    for i, (image_id, is_male) in enumerate(zip(df_celeb_image, df_gender)):
        file = os.path.join(image_folder, image_id)
        if is_male == 1:
            shutil.copy(file, male_folder)
        else:
            shutil.copy(file, female_folder)
    
    print(f"{i} files copied")
    return
    