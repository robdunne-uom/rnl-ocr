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
import string

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
					'''
						TO DO: Needs to be multithreaded
					'''
					self.processImage(path, img, fp)
	
	def processImage(self, path, img, fp):
		print('Processing {}...'.format(img))
		#print(pytesseract.image_to_string(Image.open(path+img)))
	
		imgData = pytesseract.image_to_string(Image.open(path+img))
		imgData = [s.strip() for s in imgData.splitlines()]
	
		# Try to validate the text
		imgData = self.validateText(imgData)
	
		# Prepend the image name to the data list
		imgData.insert(0, img)
	
		# Write the data to the CSV file
		a = csv.writer(fp, delimiter=',')
		a.writerows([imgData])
		
	def validateText(self, imgData):
		# TO DO: Check that the output seems reasonable, and not garbage
		# Some help here: https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality#dictionaries-word-lists-and-patterns
		id = []
		
		# Loop through the list
		for entry in imgData:
			# Validate
			entry = self.removeNonASCII(entry)
			entry = self.filterPunctuation(entry)
			
			id.append(entry)
			
		# Return the updated list
		return id
		
	def categoriseText(self):
		# Check the text against expected word lists - species, genus, location etc
		
		# Try to categorise the text using fuzzy string matching
		# http://streamhacker.com/2011/10/31/fuzzy-string-matching-python/
		
		pass
	
	def removeNonASCII(self, text):
		return ''.join([i if ord(i) < 128 else ' ' for i in text])
	
	def filterPunctuation(self, text):
		return text.translate({ord(i):None for i in "()/\\\"'!@£$%^&*#{}[]?<>~`=-_+±§€"})


RNLOCR()
