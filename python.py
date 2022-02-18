import cv2;
vedio= cv2.VideoCapture("VID_6.mp4")
i=13221
l=0
tr,img=vedio.read()
while tr:
    tr,img=vedio.read()
    if tr:
        if l==3:
            cv2.imwrite("out_VID_6/"+str(i)+".jpg",img)
            i+=1
            l=0
        l+=1
vedio.release()
print(str(i)+"\n"+"end")