import cv2;
import random;
i=0
l=[]
for i in range(0,751):
    while True:
        u= random.randint(0,1464)
        if not(u in l):
            l.append(u)
            break
    image= cv2.imread("out_VID_1/"+str(u)+".jpg")
    cv2.imwrite("out_gen/"+str(i)+".jpg",image)
print(str(i)+"\n"+"end")