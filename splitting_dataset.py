import os
from shutil import copyfile
import numpy as np

train_ratio=0.8
test_ratio=0.2
source_dir=os.path.join('105_classes_pins_dataset')
dir_list=os.listdir(source_dir)
print(len(dir_list))

train_dir=os.path.join('train')
test_dir = os.path.join('test')
os.makedirs(train_dir,exist_ok=True)
os.makedirs(test_dir,exist_ok=True)

dir_list = os.listdir(source_dir)

for folder in dir_list:
    data_dir = os.listdir(os.path.join(source_dir,folder))
    np.random.shuffle(data_dir)                            #Shuffling the examples of the classes inside the dataset.
    os.makedirs(os.path.join(train_dir , folder), exist_ok=True)
    os.makedirs(os.path.join(test_dir , folder), exist_ok=True)
    train_data = data_dir[:int(len(data_dir)*train_ratio+1)] #Splitting the training dataset with respect to the train_ratio.
    test_data = data_dir[-int(len(data_dir)*test_ratio):]

    for image in train_data:
        copyfile(os.path.join(source_dir , folder , image),os.path.join( train_dir , folder , image)) #Copying the Training files from dataset to training directory.

    for image in test_data:
        copyfile(os.path.join(source_dir , folder , image),os.path.join( test_dir , folder , image))
