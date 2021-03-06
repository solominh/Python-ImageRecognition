import cv2
import os
print(cv2.__version__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path=os.path.join(BASE_DIR,'typing_game_image.png')
image_rel_path='./typing_game_image.png'
image = cv2.imread(image_rel_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayscale_image.png',gray_image)
# cv2.imshow("Over the Clouds", image)
# cv2.imshow("Over the Clouds - gray", gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
