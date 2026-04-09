import os
import shutil
import random

SOURCE_DIR = 'dataset/plantvillage'
OUTPUT_DIR = 'dataset'
SPLIT_RATIO = 0.8

all_classes = os.listdir(SOURCE_DIR)
#To read all the classes in the dataset and store them in a list called all_classes.


print(f"Found {len(all_classes)} disease classes")
print("Starting dataset split...\n")

#loop for each folder (disease) to split the images into training and testing sets.
for class_name in all_classes:
    class_dir = os.path.join(SOURCE_DIR, class_name)
    #building the full path to this class folder

    if not os.path.isdir(class_dir):
        continue
    #skip if it's not a  folder

    all_images = os.listdir(class_dir)
    #to get a list of all the images in this class folder
    
    all_images=[
        img for img in all_images
        if img.lower().endswith(('.jpg', '.jpeg', '.png'))
    ]
    #filter to keep only actual images and removing any hidden files or non-image files that might be present in the directory.

    random.shuffle(all_images)
    #to ensure good mix of data for training and testing

    split_point=int(len(all_images) * SPLIT_RATIO)
    #calculates the split point 1000*0.8=800

    train_images=all_images[:split_point]   #80%
    val_images=all_images[split_point:]     #20%

    #output folders
    
    train_class_dir=os.path.join(OUTPUT_DIR, 'train', class_name)
    val_class_dir=os.path.join(OUTPUT_DIR, 'val', class_name)
    #for creating paths

    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(val_class_dir, exist_ok=True)

    for img in train_images:
        src=os.path.join(class_dir, img)    #source path
        dst=os.path.join(train_class_dir, img) #destination path
        shutil.copy2(src, dst)   #copy2 copies the file along with its metadata

    for img in val_images:
        src=os.path.join(class_dir, img)   
        dst=os.path.join(val_class_dir, img)
        shutil.copy2(src, dst)  

    print(f"{class_name}")
    print(f": {len(all_images)} | Train: {len(train_images)} | Val: {len(val_images)}\n")

print("Dataset split completed!")

print("\n Final Count")

train_total=0
val_total=0

train_dir=os.path.join(OUTPUT_DIR, 'train')
val_dir=os.path.join(OUTPUT_DIR, 'val')

for class_name in os.listdir(train_dir):
    train_count=len(os.listdir(os.path.join(train_dir, class_name)))
    train_total+=train_count
    val_count=len(os.listdir(os.path.join(val_dir, class_name)))
    val_total+=val_count

print(f"Total Train Images: {train_total}")
print(f"Total Val Images: {val_total}") 
print(f"Total Images: {train_total + val_total}")
   