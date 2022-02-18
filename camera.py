import cv2
import time

RTSP_URL = 'rtsp://admin:a1234567@192.168.1.16:10554/Streaming/Channels/101'

# os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

cap = cv2.VideoCapture(RTSP_URL)
#out = cv2.VideoWriter('camera_1.avi',cv2.VideoWriter_fourcc('M','J','P','G'),60, (1920,1080))
cv2.namedWindow("RTSP stream", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)
pTime=0
cTime=0
while True:
    pTime=0
    cTime=0
    _, frame = cap.read()
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    #frame = cv2.resize(frame,(1200, 600))
    cv2.imshow('RTSP stream', frame)
    
    
    
    print(int(fps))
    if cv2.waitKey(1) == 27:
        cv2.imwrite("camera_2.png",frame)
        break
    
    


cap.release()
cv2.destroyAllWindows()
