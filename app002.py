# OpneCV 모듈 가져오기
import cv2

# 버전 확인
print(cv2.__version__)

#이미지 불러와서 출력하기 -()
# robotImg = cv2.imread('./res/img/humanoid.jpg') #이미지 읽기
# print(f'robotImg shape: {robotImg.shape}') #이미지 크기 -->(3715(v), 5565(h), 3(BGR))

# robotImg = cv2.resize(robotImg, (330, 565))

# cv2.imshow('title-robotImg', robotImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imshow('title-robotImg', robotImg) #이미지 출력
# cv2.waitKey(1000 * 3)                      #3초 동안 출력이 된다.

## 읽기 옵션
robotImgColor = cv2.imread('./res/img/humanoid.jpg', cv2.IMREAD_COLOR)
robotImgColor = cv2.imread(robotImgColor, (330, 565))

roobotImgGray = cv2.imread('./res/img/humanoid.jpg', cv2.IMREAD_GRAYSCALE)
roobotImgGray = cv2.imread(robotImgColor, (330, 565))

roobotImgUnchanged = cv2.imread('./res/img/humanoid.jpg', cv2.IMREAD_UNCHANGED) #ALPLA 유지
roobotImgUnchanged = cv2.imread(roobotImgUnchanged, (330, 565))

cv2.imshow('title-robotImgColor', robotImgColor)
cv2.imshow('title-robotImgColor', roobotImgGray)
cv2.imshow('title-robotImgColor', roobotImgUnchanged)

cv2.waitKey(0)
cv2.destroyAllWindows()

#동영상 불러와서 출력하기
#OpenCV에서 동영상을 불러온다는 것은 동영상 -> 프레임 추출 -> 이미지화 -> 출력

# robotMov = cv2.VideoCapture('./res/mov/humanoid.mp4')
# while robotMov.isOpened(): #동영상 파일이 연결되어 있다면..
#     result, frame = robotMov.read()  #result: read 성공 여부, frame: 받아온 이미지(프레임)
#     if not result:
#         print('End FRAME')
#         break
    
#     #사이즈 조정
#     frame = cv2.resize(frame, (330, 565))


#     print(f'frame: {frame}')
#     cv2.imshow('title-robotFrame', frame)    #매우 빠르게 frame이 출력된다.

#     if cv2.waitKey(1) == ord('q'): #1ms 동안 기다린다. 사용자가 'q'를 입력하면 중단한다. 
#                                        #숫자가 클 수록 재생속도가 느리다
#         break

# robotMov.release()
# cv2.destroyAllWindows() #윈도우 다 닫기

#캠에서 동영상 실시간으로 불러오기
'''
robotMov = cv2.VideoCapture(0)
while robotMov.isOpened(): #동영상 파일이 연결되어 있다면..
    result, frame = robotMov.read()  #result: read 성공 여부, frame: 받아온 이미지(프레임)
    if not result:
        print('End FRAME')
        break
    
    #사이즈 조정
    frame = cv2.resize(frame, (330, 565))


    print(f'frame: {frame}')
    cv2.imshow('title-robotFrame', frame)    #매우 빠르게 frame이 출력된다.

    if cv2.waitKey(1) == ord('q'): #1ms 동안 기다린다. 사용자가 'q'를 입력하면 중단한다.
        break

robotMov.release()
cv2.destroyAllWindows() #윈도우 다 닫기
'''
