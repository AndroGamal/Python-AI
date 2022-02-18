import cv2;
import random;
l=[1465,3149,4028,8829,13221,14999]
k=[1465,3149,4028,8829,13221,14999]
z=751
for i in range(751,901):
    for r in range(2,7):
        while True:
            u= random.randint(k[r-2],k[r-1])
            if not(u in l):
                l.append(u)
                break
        image= cv2.imread("out_VID_"+str(r)+"/"+str(u)+".jpg")
        cv2.imwrite("out_gen/"+str(z)+".jpg",image)
        z+=1
print(str(i)+"\n"+"end")