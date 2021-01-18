import os
import shutil

data_directories = ['train', 'validation', 'test']
target_directories = ['cat', 'dog']


def populate_base_dir(original_dataset_dir):
    original_path = os.curdir
    os.chdir(original_dataset_dir)

    # Push data to train folder
    shutil.unpack_archive('train.zip', 'train', 'zip')
    shutil.move('train/train/*', 'train')

    # clean up
    shutil.rmtree('train/train/')
    os.remove('train.zip')

    # go back to the top
    os.chdir(original_path)


def init_dataset_directories(base_dir: str, directories: dict):
    os.mkdir(base_dir)

    # Create train, validation and test directories
    for data_dir in data_directories:
        directories[data_dir] = os.path.join(base_dir, data_dir)
        os.mkdir(directories[data_dir])

        for target_dir in target_directories:
            sub_dir = f"{data_dir}_{target_dir}"
            directories[sub_dir] = os.path.join(
                directories[data_dir], target_dir)
            os.mkdir(directories[sub_dir])

    return directories


def populate_dataset_directories(original_dataset_dir: str, directories: dict):
    source_train_dir = f'{original_dataset_dir}/train'

    # Fill into the directories the train data
    for target_dir in target_directories:
        fnames = ['{}.{}.jpg'.format(target_dir, i) for i in range(0, 1000)]
        # Train Data
        for fname in fnames:
            src = os.path.join(source_train_dir, fname)
            dst = os.path.join(directories[f'train_{target_dir}'], fname)
            shutil.copyfile(src, dst)

        # Test Data
        fnames = ['{}.{}.jpg'.format(target_dir, i) for i in range(1000, 1500)]
        for fname in fnames:
            src = os.path.join(source_train_dir, fname)
            dst = os.path.join(directories[f'test_{target_dir}'], fname)
            shutil.copyfile(src, dst)

        # Validation Data
        fnames = ['{}.{}.jpg'.format(target_dir, i) for i in range(1500, 2000)]
        for fname in fnames:
            src = os.path.join(source_train_dir, fname)
            dst = os.path.join(directories[f'validation_{target_dir}'], fname)
            shutil.copyfile(src, dst)

    return directories


def set_up_cat_dogs_small_dataset():
    original_dataset_dir = 'kaggle_original_data'
    base_dir = 'cats_and_dogs_small'
    directories: dict = {}

    os.mkdir(base_dir)
    populate_base_dir(original_dataset_dir)
    directories = init_dataset_directories(base_dir, directories)
    directories = populate_dataset_directories(
        original_dataset_dir, directories)

    return directories
