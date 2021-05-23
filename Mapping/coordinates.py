import cv2
#reading the image
img = cv2.imread('img3_resized_grid.jpg', cv2.IMREAD_UNCHANGED)
#displaying the image
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#entering the coordinates of the image displayed
string = raw_input()
#different formats of the coordinates
#coord - list of string of 1st coordinates
coord = string.split()
#coord2 - list of tuple of (x,y) coordinates
coord2 = [(int(int(i)/20),int(i)-(int(int(i)/20)*20)) for i in coord]
#coord2s - list of string of (x,y) coordinates
coord2s = [str(i) for i in coord2]
#coords - string of all (x,y) coordinates
coords = ',_'.join(coord2s)
#displaying the string of all (x,y) coordinates
#print(coords)
#writing all the coordinates (x,y) to the file
with open("coords.txt", "w") as file:
    for i in coord2s:
        file.write(i+'\n')