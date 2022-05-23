import cv2
import face_recognition
#1.1 读取图片
jay = cv2.imread('jay.jpg')
img = cv2.imread('jay1.jpg')
#1.2 获取人脸位置
locations = face_recognition.face_locations(img)
#对人脸进行编码
jay_face_encoding = face_recognition.face_encodings(jay)[0]
known_face_encodings = [jay_face_encoding]
known_face_names = ['jay']

unknown_face_encodings = face_recognition.face_encodings(img, locations)
#a:[1,2]
#b:['a','b']
#zip(a,b) => [(1,'a'),(2,'b')]

for (top, right, bottom, left), face_encoding in zip(locations, unknown_face_encodings):
    #1.3 使用方框，把人脸框起来
    cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
    matchs = face_recognition.compare_faces(known_face_encodings, face_encoding, 0.4)
    name = 'unknown'
    for match, known_name in zip(matchs, known_face_names):
        if match:
            name = known_name
            break
    #标记姓名
    cv2.putText(img, name, (left, top-20), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0, 0, 255), 2)
#2. 展示
cv2.imshow('jay', img)
#3. 等待键盘事件
cv2.waitKey(0)
#4. 销毁窗口
cv2.destroyAllWindows()