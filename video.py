import cv2
vc = cv2.VideoCapture(0)
while True:
    ret, img = vc.read()
    if not ret:
        print('没有捕获到视频')
        break
    cv2.imshow('DYT', img)
    if cv2.waitKey(1) != -1:
         vc.release()
         cv2.destroyAllWindows()
         break
         