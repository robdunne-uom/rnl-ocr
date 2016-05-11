#!/usr/bin/env python

'''

Generate text label data for RNL images.

Prerequisites:
	- Python 3
	- PyTesseract: https://github.com/madmaze/pytesseract and it's dependecies (Google Tesseract OCR, PIL)
		- sudo pip install pillow
		- sudo pip install pytesseract
		- brew install tesseract

'''

import os
import pytesseract
from PIL import Image
import csv

class RNLOCR():
	'Main class for reading the label data in images'

	# Constructor
	def __init__(self):
		self.scanImages()
	
	def scanImages(self):
		# Loop through the files in the images folder	
		path = '../images/'
		dataFile = '../data/data.csv'
		
		with open(dataFile, 'w+', newline='') as fp:
			for img in os.listdir(path):
				if os.path.isfile(path+img):
					print('Processing {}...'.format(img))
					#print(pytesseract.image_to_string(Image.open(path+img)))
					
					imgData = pytesseract.image_to_string(Image.open(path+img))
					imgData = imgData.split('\n', 1)
					imgData.insert(0, img)
					
					a = csv.writer(fp, delimiter=',');
					data = [imgData];
					a.writerows(data);
		
	def validateText(self):
		# TO DO: Check that the output seems reasonable, and not garbage
		# Some help here: https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality#dictionaries-word-lists-and-patterns
		
		pass
	
	def categoriseText(self):
		# Check the text against expected word lists - species, genus, location etc
		
		# Try to categorise the text using fuzzy string matching
		# http://streamhacker.com/2011/10/31/fuzzy-string-matching-python/
		
		pass

RNLOCR()
