
import pyautogui
import cv2
from subprocess import call


def take_screenshot():
    output = 'screenshot.png'
    # region = (200, 200, 600, 600)
    region = (760, 300, 836, 514)
    pyautogui.screenshot(output, region=region)
    print('Take screenshot done!')


def black_white_image():
    screenshot = './screenshot.png'
    image = cv2.imread(screenshot)

    # cv2.imshow('Image', image)
    # cv2.waitKey(0)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite(screenshot, thresh)

    # cv2.imshow('Image', thresh)
    # cv2.waitKey(0)

    print('Create black white screenshot done!')
    # cv2.imshow("Image", thresh)
    # cv2.waitKey(0)


def extract_text_from_image():
    input = './screenshot.png'
    output = 'text_recognition_result'
    call(["tesseract", input, output])
    print("Tesseract done!")


def send_keyboard_event():
    file_path = './text_recognition_result.txt'
    text_lines = []
    with open(file_path) as f:
        text_lines = list(f)

    print('Read text file done!')
    print(text_lines)

    if text_lines:
        for line in reversed(text_lines):
            cleaned_line = line.strip()
            if cleaned_line:
                print(cleaned_line)
                pyautogui.typewrite(cleaned_line.lower())
        print('Sending keyboard done')
    else:
        print('Fail')


def main():
    take_screenshot()
    black_white_image()
    extract_text_from_image()
    send_keyboard_event()
