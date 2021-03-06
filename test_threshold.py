import cv2
im_gray = cv2.imread('./grayscale_image.png')
# (thresh, im_bw) = cv2.threshold(im_gray, 128,
                                # 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 240
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]

# show the image
cv2.imshow("Image", im_bw)
cv2.waitKey(0)
cv2.imwrite('blackwhite_image.png', im_bw)
