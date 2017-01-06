from subprocess import call

image = './blackwhite_image.png'
output = 'text_recognition_result'
call(["tesseract", image, output])
