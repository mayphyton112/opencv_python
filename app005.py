import cv2

url = 'http://192.168.137.173:81s/stream'

cap= cv2.VideoCapture(url, cv2.CAP_FFMPEG)

while True:
    ret, frame = cap.read()

    if not ret:
        print('프레임 읽기 실패')
        continue
    cv2.imshow('ESP32-CAM', frame) #창의 이름, 출력할 이미지

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()