# rnl-ocr

Generate text label data for RNL images.

Prerequisites:
	
	- Python 3
	
	- PyTesseract: https://github.com/madmaze/pytesseract and it's dependecies (Google Tesseract OCR, PIL)
	
		- sudo pip install pillow
		- sudo pip install pytesseract
		- brew install tesseract
		
To run: 

<pre>
<code>
cd ./code
python3 rnlocr.py
</code>
</pre>

Outputs a CSV file to ./data/data.csv
