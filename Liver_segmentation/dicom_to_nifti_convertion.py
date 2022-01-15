# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 23:00:02 2022

@author: mahfuz
"""

from glob import glob
import shutil
import os
import dicom2nifti

in_path_images=r'C:\Users\mahfu\Desktop\Codes\dicom_groups\images'
in_path_lables=r'C:\Users\mahfu\Desktop\Codes\dicom_groups\labels'

out_path_images=r'C:\Users\mahfu\Desktop\Codes\nifiti_files\images'
out_path_lables=r'C:\Users\mahfu\Desktop\Codes\nifiti_files\lables'

list_images=glob(in_path_images)
list_lables=glob(in_path_lables)

for patient in list_images:
    patient_name=os.path.basename(os.path.normcase(patient))
    dicom2nifti.dicom_series_to_nifti(patient,os.path.join(out_path_images,patient_name+'.nii.gz'))
    
    
for patient in list_lables:
    patient_name=os.path.basename(os.path.normcase(patient))
    dicom2nifti.dicom_series_to_nifti(patient,os.path.join(out_path_lables,patient_name+'.nii.gz'))





