import pyautogui
import cv2

output = 'screenshot.png'
region = (200, 200, 600, 600)
pyautogui.screenshot(output, region=region)


screenshot = './screenshot.png'
image = cv2.imread(screenshot)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("Image", thresh)
cv2.waitKey(0)
