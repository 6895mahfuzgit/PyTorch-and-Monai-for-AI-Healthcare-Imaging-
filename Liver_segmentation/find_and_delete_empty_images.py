# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 21:33:56 2022

@author: mahfuz
"""

from glob import glob
import nibabel as nif
import numpy as np


input_path_lables = r'C:\Users\mahfu\Desktop\Codes\nifiti_files\lables\*'
imput_labels = glob(input_path_lables)

for patient in imput_labels:
    nifti_file = nif.load(patient)
    f_data = nifti_file.get_fdata()
    np_unique = np.unique(f_data)
    print(np_unique)
    if len(np_unique) == 1:
       print('Dleted file length', len(np_unique))
    else:
        print('OK', len(np_unique))
