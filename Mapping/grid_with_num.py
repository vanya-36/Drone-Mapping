#to be executed in raspberry pi4, python 2

import cv2
# all colours in the image are blue, green, red
#importing the image
img = cv2.imread('img3.jpg', cv2.IMREAD_UNCHANGED)
#dimensions of original image
#print('Original Dimensions : ',img.shape)
#resizing image
resized = img = cv2.resize(img, (400, 400), interpolation = cv2.INTER_AREA)
#setting the font for text here - co-ordinates
font = cv2.FONT_HERSHEY_SIMPLEX
for i in range(0, 400, 20):
    #drawing grid lines
    cv2.line(img, (i, 0), (i, 400), (0, 255, 0), 1)
    cv2.line(img, (0, i), (400, i), (0, 255, 0), 1)
    for j in range(0, 20):
        #drawing numbers for co-ordinates
        cv2.putText(img, str(i+j), (j*20, i+20-5), font, 0.20, (0, 255, 0), 1, cv2.LINE_AA)
#saving the image with gridlines and co-ordinates
cv2.imwrite('img3_resized_grid.jpg',resized)
#dimensions of new image
#print('Resized Dimensions : ',resized.shape)
#displaying the image
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
