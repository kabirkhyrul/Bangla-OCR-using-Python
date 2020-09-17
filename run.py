
import pytesseract as pytesseract

import cv2 as cv2

import sys

import webbrowser

import os


# read imgae
image = cv2.imread('Untitled.png')

# convert to gray
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# get text
data = pytesseract.image_to_string(gray, lang='ben')

#write data to file with unicode
with open("output.html", "w", encoding="utf-8") as f:
	f.write("<pre>"+ data + "</pre>")
	f.close()	

# print output in console
print(data)

# get file path
filename = 'file:///'+os.getcwd()+'/' + 'output.html'

# open in new tab
webbrowser.open(filename, new=2)  