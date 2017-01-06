import cv2
image = cv2.imread('./vuong.png')
im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# (thresh, im_bw) = cv2.threshold(im_gray, 128,
                                # 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 240
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]

# show the image
cv2.imshow("Image", im_bw)
cv2.waitKey(0)
cv2.imwrite('blackwhite_image.png', im_bw)
