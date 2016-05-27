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
from multiprocessing.dummy import Pool as ThreadPool

class RNLOCR():
	'Main class for reading the label data in images'	

	# Constructor
	def __init__(self):
		self.path = '../images/'
		self.dataFile = '../data/data.csv'
		
		self.cleanUp()
		self.scanImages()
	
	def cleanUp(self):
		# Delete previous copy of the data
		try:
			os.remove(self.dataFile)
			open(self.dataFile, 'r+')
		except OSError:
			pass
	
	def scanImages(self):
		# Loop through the files in the images folder	
		pool = ThreadPool(8)
		results = pool.map(self.processImage, os.listdir(self.path))
		pool.close()
		pool.join()
	
	def processImage(self, img):
		print('Processing {}...'.format(img))
		#print(pytesseract.image_to_string(Image.open(path+img)))
		
		'''
			TO DO: Would altering the contrast of the image improve results?	
		'''
		
		if '.JPG' in img:
			with open(self.dataFile, 'a', newline='') as fp:		
				imgData = pytesseract.image_to_string(Image.open(self.path+img))
				imgData = [s.strip() for s in imgData.splitlines()]
	
				# Try to validate the text
				imgData = self.validateText(imgData)
	
				# Prepend the image name to the data list
				imgData.insert(0, img)
	
				# Write the data to the CSV file
				a = csv.writer(fp, delimiter=',')
				a.writerows([imgData])
		
	def validateText(self, imgData):
		# TO DO: Check that the output seems reasonable, and not garbage. Normalise where possible.
		# Some help here: https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality#dictionaries-word-lists-and-patterns
		id = []
		
		# Loop through the list
		for entry in imgData:
			# Validate
			entry = self.removeNonASCII(entry)
			entry = self.filterPunctuation(entry)
			entry = self.trimSpaces(entry)
			
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
		return text.translate({ord(i):None for i in "()/\\\"'!@£$%^&*#{}[]?<>~`=-_+±§€.,"})

	def trimSpaces(self, text):
		return text.strip()
	

RNLOCR()
