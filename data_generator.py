import os
import random
from shutil import copyfile

print(len(os.listdir('data/source/with_mask')))
print(len(os.listdir('data/source/without_mask')))

class DataGenerator:
    
    def create_directory(self):
        try:
            base = 'data/face-mask'

            train_dir = os.path.join(base,'train')
            test_dir = os.path.join(base,'test')

            train_with_mask_dir = os.path.join(train_dir,'with_mask')
            train_without_mask_dir = os.path.join(train_dir,'without_mask')

            test_with_mask_dir = os.path.join(test_dir,'with_mask')
            test_without_mask_dir = os.path.join(test_dir,'without_mask')

            os.mkdir(base)

            os.mkdir(train_dir)
            os.mkdir(test_dir)

            os.mkdir(train_with_mask_dir)
            os.mkdir(train_without_mask_dir)

            os.mkdir(test_with_mask_dir)
            os.mkdir(test_without_mask_dir)
        except OSError:
            pass
    
    def split_data(self,SOURCE, TRAINING, TESTING, SPLIT_SIZE):
        list = os.listdir(SOURCE)
        all_files = []
        for f in list :
            file_path = SOURCE +'/'+ f
            if os.path.getsize(file_path):
                all_files.append(f)
            else:
                print('files not found')

        split_val = int(len(all_files)*SPLIT_SIZE)
        shuffled_list = random.sample(all_files,len(all_files))
        train_file = shuffled_list[:split_val]
        test_file = shuffled_list[split_val:]
        for f in train_file:
            copyfile(SOURCE+'/'+f,TRAINING+'/'+f)
        for f in test_file:
            copyfile(SOURCE+'/'+f,TESTING+'/'+f)
    
    def copy_data_to_dest(self):
        with_mask_source_dir = 'data/source/with_mask'
        with_mask_train_dir = 'data/face-mask/train/with_mask'
        with_mask_test_dir = 'data/face-mask/test/with_mask'

        without_mask_source_dir = 'data/source/without_mask'
        without_mask_train_dir = 'data/face-mask/train/without_mask'
        without_mask_test_dir = 'data/face-mask/test/without_mask'

        split_size = .8
        
        self.create_directory()
        self.split_data(with_mask_source_dir, with_mask_train_dir, with_mask_test_dir, split_size)
        self.split_data(without_mask_source_dir, without_mask_train_dir, without_mask_test_dir, split_size)