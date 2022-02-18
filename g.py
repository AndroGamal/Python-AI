from email.mime import image
import cv2
image= cv2.imread("camera_2.png")
i=0
l=cv2.line(image,(1723,590),(1425,542),0,10)
cv2.imshow("s",l)
cv2.waitKey(0)
cv2.destroyAllWindows()