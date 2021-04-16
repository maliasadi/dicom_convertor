#!/usr/bin/python

import sys
import os 
import glob
import pydicom
import numpy as np

from PIL import Image
from pydicom.data import get_testdata_file

COUNTER = 0

def update_destination_file_name (file_name):
	"""
	Update destination file_name with adding `COUNTER` to the beginning 
	"""
	global COUNTER 
	COUNTER += 1
	splitted = file_name.split('/')
	return file_name[:len(file_name)-len(splited[-1])] + 'Image%05d' % COUNTER +'_'+splited[-1]


def convert_to_dicom(file_name):
	"""
	Convert bmp to dicom using pydicom 
	"""
	path = get_testdata_file("CT_small.dcm")
	ds = pydicom.dcmread(path)
	img = Image.open(file_name+".bmp")
	npa = np.asarray(img)
	ds.PixelData = img.tobytes()
	name = update_destination_file_name(file_name)
	ds.save_as(name+'.dcm')
	print("DONE\t "+name+".dcm")
	
def img2dcm_from_bmp(file_name):
	"""
	Convert bmp to dicom using img2dcm from dcmtl 
	To install: brew install dcmtk
	"""
	name = update_destination_file_name(file_name)
	os.system('img2dcm -i BMP '+file_name+'.bmp '+name+'.dcm ')	
	print("DONE\t "+name+".dcm")

def get_file_names(DIR):
	"""
	Get name of bmp files in DIR
	"""
	return sorted(glob.glob(DIR+"*.bmp"))

if __name__ == '__main__':
	if len(sys.argv) != 3 or sys.argv[1] in ["--help", "-h"]:
		print(f"TRY\t $ python {sys.argv[0]} [0 => pydicom, 1 => dcmtl] [directory_path]")
		sys.exit()

	DIR = sys.argv[2]
	if DIR[-1] != '/':
		DIR = DIR+"/"

	file_names = get_file_names(DIR)
	if int(sys.argv[1]) == 0:
		print("RUN\t pydicom...")
		for name in file_names:
			convert_to_dicom(name[:-4])
	else:
		print("RUN\t dcmtl...")
		for name in file_names:
			img2dcm_from_bmp(name[:-4])

	# print(COUNTER)