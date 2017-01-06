import pyautogui

# pyautogui.press('a')
output = 'screenshot.png'
region = (200, 200, 600, 600)

pyautogui.screenshot(output, region)
