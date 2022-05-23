import cv2
img = cv2.imread('1.jpg')
cv2.rectangle(img,(200,300),(400,500),(255,0,0),2)
cv2.putText(img,'jay',(200,300-20),cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0,0,255))
cv2.imshow('jay',img)
cv2.waitKey()
cv2.destroyAllWindows()