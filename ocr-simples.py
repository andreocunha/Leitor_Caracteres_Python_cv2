import cv2
import numpy as np
import pytesseract #Vai reconhecer os caracteres dentro da imagem reconhecida

img = cv2.imread("4.png")
img = cv2.resize(img, None, fx=1.5, fy=1.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 1)

config = "--psm 4"
text = pytesseract.image_to_string(adaptive_threshold)
print(text)

cv2.imshow("Adaptive", adaptive_threshold)
cv2.waitKey(0)
