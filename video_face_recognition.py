import cv2
import face_recognition
#1. 准备人脸库
#1.1 读取图片
me = cv2.imread('dyt.jpg')
he = cv2.imread('huateng1.jpg')

#1.2 对图片中人脸进行编码
me_face_enconding = face_recognition.face_encodings(me)[0]
he_face_enconding = face_recognition.face_encodings(he)[0]

#1.3 准备人脸库的人脸编码列表
known_face_encodings = [me_face_enconding, he_face_enconding]

#1.4 准备人脸库中人脸编码对应姓名
known_face_names = ['me','he']

#2. 捕获视频中图片
vc = cv2.VideoCapture(0)
while True:
    # 获取视频中，每一帧的图片；
    ret, img = vc.read()
    if not ret:
        print('没有捕获到视频')
        break
    # 3. 发现视频中国图片中人脸位置
    # 3.1 发现图片中人脸的位置
    locations = face_recognition.face_locations(img)
    # 3.2 图片中人脸进行编码
    face_encondings = face_recognition.face_encodings(img, locations)
    # 遍历 locations, face_encodings, 识别图片中人脸
    # locationL: top, right, bottom, left
    for (top, right, bottom, left), face_encoding in zip(locations, face_encondings):
        # 比较人脸
        # 4. 识别视频中图片中人脸的姓名
        matchs = face_recognition.compare_faces(known_face_encodings, face_encoding, 0.4)
        name = "unknown"
        for match, known_name in zip(matchs, known_face_names):
            if match:
                name = known_name
                break
        # 4.1 标记人脸的位置
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

        # 4.2 标记人脸的姓名
        cv2.putText(img, name, (left, top-20), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0,0,255), 2)

    #5. 展示
    cv2.imshow('Video', img)

    #6.释放资源
    if cv2.waitKey(1) != -1:
        # 关闭摄像头
        vc.release()
        # 销毁窗口
        cv2.destroyAllWindows()
        # 结束循环
        break