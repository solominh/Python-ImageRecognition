import pyautogui
import cv2
import time

time.sleep(3)
# pyautogui.press('a')
output = 'screenshot.png'
# region = (200, 200, 600, 600)
region = (760, 300, 836, 514)
pyautogui.screenshot(output, region)

screenshot = './screenshot.png'
image = cv2.imread(screenshot)

cv2.imshow('Image', image)
cv2.waitKey(0)
