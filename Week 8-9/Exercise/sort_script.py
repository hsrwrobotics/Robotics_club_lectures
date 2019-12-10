# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:25:03 2019

@author: batho
"""

import os
import shutil

image_name=sorted(os.listdir('dogs-vs-cats\\train\\train'))

#print(image_name[:4])

def copy_files(prefix_str, range_start, range_end, target_dir):
    image_paths=[os.path.join('dogs-vs-cats\\train\\train', prefix_str+'.'+str(i)+'.jpg') for i in range(range_start, range_end)]
    dest_dir=os.path.join('data', target_dir, prefix_str)
    os.makedirs(dest_dir)
    for image_path in image_paths:
        shutil.copy(image_path, dest_dir)
        
copy_files('dog', 0,1000,'train')
copy_files('cat', 0, 1000, 'train')
copy_files('dog', 1000, 1400, 'test')
copy_files('cat', 1000, 1400, 'test')
