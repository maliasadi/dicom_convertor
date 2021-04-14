#!/usr/bin/python

import sys
import numpy as np
import pydicom
import glob
from PIL import Image
from pydicom.dataset import Dataset, FileDataset
from pydicom.data import get_testdata_file

def convert_to_diom(file_name):
	"""
	Convert bmp to dicom
	"""
	path = get_testdata_file("CT_small.dcm")
	ds = pydicom.dcmread(path)
	img = Image.open(file_name+".bmp")
	npa = np.asarray(img)
	ds.PixelData = img.tobytes()
	ds.save_as(file_name+".dcm")
	print(file_name+".dcm"+"... DONE")
	
def get_file_names(DIR):
	"""
	Get name of bmp files in DIR
	"""
	return glob.glob(DIR+"*.bmp")

if __name__ == '__main__':
	if len(sys.argv) != 2 or sys.argv[1] in ["--help", "-h"]:
		print(f"TRY	 $ python {sys.argv[0]} directory_path")
		sys.exit()

	DIR = sys.argv[1]
	if DIR[-1] != '/':
		DIR = DIR+"/"

	for name in get_file_names(DIR):
		convert_to_diom(name[:-4])
