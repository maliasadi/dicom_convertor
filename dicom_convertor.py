#!/usr/bin/python

import sys
import os 
import numpy as np
import pydicom
import glob
from PIL import Image
from pydicom.data import get_testdata_file

def convert_to_dicom(file_name):
	"""
	Convert bmp to dicom using pydicom 
	"""
	path = get_testdata_file("CT_small.dcm")
	ds = pydicom.dcmread(path)
	img = Image.open(file_name+".bmp")
	npa = np.asarray(img)
	ds.PixelData = img.tobytes()
	ds.save_as(file_name+".dcm")
	print(file_name+".dcm"+"... DONE")
	
def img2dcm_from_bmp(file_name):
	"""
	Convert bmp to dicom using img2dcm from dcmtl 
	To install: brew install dcmtk
	"""
	os.system('img2dcm -i BMP '+file_name+'.bmp '+file_name+'.dcm ')	
	print(file_name+".dcm"+"... DONE")

def get_file_names(DIR):
	"""
	Get name of bmp files in DIR
	"""
	return glob.glob(DIR+"*.bmp")

if __name__ == '__main__':
	if len(sys.argv) != 3 or sys.argv[1] in ["--help", "-h"]:
		print(f"$ python {sys.argv[0]} type directory_path")
		print("type: 0 => pydicom")
		print("      1 => dcmtl")
		sys.exit()

	DIR = sys.argv[2]
	if DIR[-1] != '/':
		DIR = DIR+"/"

	file_names = get_file_names(DIR)
	if int(sys.argv[1]) == 0:
		for name in file_names:
			convert_to_dicom(name[:-4])
	else:
		for name in file_names:
			img2dcm_from_bmp(name[:-4])