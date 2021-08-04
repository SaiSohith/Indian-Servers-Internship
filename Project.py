import cv2
from operator import itemgetter

top_left_corner=[]
bottom_right_corner=[]


def drawRectangle(action, x, y, flags, param):
  global top_left_corner, bottom_right_corner

  if action == cv2.EVENT_LBUTTONDOWN:
    top_left_corner = [(x,y)]
    # cv2.rectangle(image, top_left_corner[0], (0,255,0),2, 8)
    
  elif action == cv2.EVENT_LBUTTONUP:
    bottom_right_corner = [(x,y)]
    cv2.rectangle(image, top_left_corner[0], bottom_right_corner[0], (0,255,0),2)
    cv2.imshow("Window",image)
    # print(top_left_corner)
    # print(bottom_right_corner)
    p1 = list(map(itemgetter(0),top_left_corner))
    p2= list(map(itemgetter(1),top_left_corner))
    m1 =list(map(itemgetter(0),bottom_right_corner))
    m2= list(map(itemgetter(1),bottom_right_corner))

    x1=p2[0]
    x2=p1[0]
    y1=m2[0]
    y2=m1[0]
    # print(p1,"",p2)
    # print(m1," ",m2)
    cropped_image = pic[x1:y1 , x2 : y2]
    cv2.imshow("cropped", cropped_image)
    cv2.imwrite("Cropped Image.jpg", cropped_image)
  


Source=input("Enter the Source Path of Image:")
image =cv2.imread(Source)
cv2.namedWindow("Window")
cv2.imshow("Window", image)
pic=cv2.imread(Source)

cv2.setMouseCallback("Window", drawRectangle)


cv2.waitKey(0)
cv2.destroyAllWindows()