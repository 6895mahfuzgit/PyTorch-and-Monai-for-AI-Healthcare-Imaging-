# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from glob import glob
import shutil
import os


in_path=r'C:\Users\mahfu\Desktop\Codes\dicom_files\images'
out_path=r'C:\Users\mahfu\Desktop\Codes\dicom_groups\images'

# patient_list=glob(in_path+'/*')
# print(patient_list[0])

for patient in glob(in_path+'/*'):
    patient_name=os.path.basename(os.path.normcase(patient))
    number_folders=int(len(glob(patient+'/*'))/64)
    # print(number_folders )
    # print(patient_name)
    for i in range(number_folders):
        out_path_name=os.path.join(out_path, patient_name+'_'+str(i))
        print(out_path_name)
        os.mkdir(out_path_name)
        for i,file in enumerate(glob(patient+'/*')):
             if i== 64 + 1 :
                break
             shutil.move(file, out_path_name) 
        

