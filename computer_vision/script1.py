import cv2

# 0 is black-coloured
img = cv2.imread("galaxy.jpg", 0)

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()