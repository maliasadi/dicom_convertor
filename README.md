# DICOM Convertor
A python script to convert **BMP** files to **DICOM**.

## How To Use?
``` 
$ python3 dicom_convertor.py
TRY	 $ python dicom_convertor.py [0 => pydicom, 1 => dcmtl] [directory_path]
```

To use [*pydicom*](https://pydicom.github.io/): converting *lena.bmp* to *lena.dcm*, try  
```
$ python3 dicom_convertor.py 0 .
RUN	 pydicom...
DONE	 ./Image00001_lena.dcm
```

To use [*dcmtl*](https://support.dcmtk.org/docs/img2dcm.html): converting *lena.bmp* to *lena.dcm*, try  
```
$ python3 dicom_convertor.py 1 .
RUN	 dcmtl...
DONE	 ./Image00001_lena.dcm
```

## References
1. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3354356/
2. https://pydicom.github.io/
3. https://support.dcmtk.org/docs/img2dcm.html