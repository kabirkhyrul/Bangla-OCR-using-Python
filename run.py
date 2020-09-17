
import pytesseract as pytesseract

import cv2 as cv2

import sys

import webbrowser

import os

#  For Excel (optional). Comment out this line
import xlsxwriter
from datetime import date

# read imgae
image = cv2.imread('Untitled.png')

# convert to gray
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# get text
data = pytesseract.image_to_string(gray, lang='ben')

# ========================= Excel Output ====================================
# Create an new Excel file and add a worksheet.
# workbook = xlsxwriter.Workbook(date.today().isoformat()+'.xlsx');
# worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
# worksheet.set_column('A:A', 20)

#Making Array from data String
# arr = data.split('\n')

# for k, v in enumerate(arr):   
# 	worksheet.write('A'+ str(k+1), v)

# workbook.close()

# ======================== File Output ======================================
# write data to file with unicode
with open(date.today().isoformat()+".txt", "w", encoding="utf-8") as f:
	f.write("<pre>"+ data + "</pre>")
	f.close()	

# print output in console
print(data)

#HTML Output

# get file path
# filename = 'file:///'+os.getcwd()+'/' + date.today().isoformat()+'.html'

# open in new tab
# webbrowser.open(filename, new=2)  


