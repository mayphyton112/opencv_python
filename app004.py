import cv2
import numpy as np

#  원 생성
'''
circleBG = np.zeros((480, 640, 3), dtype=np.uint8)
COLOR = (255, 255, 0)  #색상
RADIUS = 100           #반지름
THICKNESS = 3          # 테두리 선 두께

cv2.circle(circleBG,              (150, 150), RADIUS,  COLOR, THICKNESS, cv2.LINE_AA)
#          어디에 그릴 것인가       중심점       반지름    색상    두께            선 타입


cv2.circle(circleBG,              (450, 150), RADIUS,  COLOR, cv2.FILLED, cv2.LINE_AA)
#          어디에 그릴 것인가       중심점       반지름    색상    안을 채운다.            선 타입

cv2. imshow('title-circle', circleBG)
cv2.waitKey(0)
cv2.destroyAllWindows
'''

#사각형 그리기
'''
rectangleBG = np.zeros((480, 640, 3), dtype=np.uint8)
COLOR = (255, 255, 0)  #색상          
THICKNESS = 3          # 테두리 선 두께

cv2.rectangle(rectangleBG,              (50, 150), (200, 200), COLOR, THICKNESS, cv2.LINE_AA)
#          어디에 그릴 것인가        좌상단좌표       우하단좌표    색상    두께            선 타입


cv2.rectangle(rectangleBG,             (300, 100), (500, 300),   COLOR, cv2.FILLED, cv2.LINE_AA)
#          어디에 그릴 것인가            좌상단      우하단       색상    안을 채운다.            선 타입

cv2. imshow('title-circle', rectangleBG)
cv2.waitKey(0)
cv2.destroyAllWindows
'''

## 다각형 그리기
'''
polygonBG = np.zeros((380, 640, 3), dtype=np.uint8)

COLOR = (255, 255, 0)   #색상
THICKNESS = 3           #두께

points01 = np.array([
    [50, 50],
    [150, 150],
    [50, 150],
])

points02 = np.array([
    [250, 50],
    [350, 150],
    [250, 150],
])
cv2.polylines(polygonBG,    [points01],        True,          COLOR, THICKNESS, cv2.LINE_AA)  #다각형을 그린다.
#             어디에 그릴지   어떤 것을 그릴지  닫힌형 or 열린도형  색상     두께          라인타입
# 리스트인 이유는 여러 개를 같이 그릴 수 있기 때문

cv2.polylines(polygonBG,    [points02],        True,          COLOR, THICKNESS, cv2.LINE_AA)  #다각형을 그린다.
#             어디에 그릴지   어떤 것을 그릴지  닫힌형 or 열린도형  색상     두께          라인타입

cv2.imshow('title-polygonBG', polygonBG)
cv2. waitKey(0)
cv2.destroyAllWindows
'''

##이미지 복사& 저장
'''
robotImgGrayscale = cv2.imread('./res/img/humanoid.jpg', cv2.IMREAD_GRAYSCALE)
robotImgGrayscale = cv2.resize(robotImgGrayscale, (330, 565))
cv2.imshow('title-robotImgGrayscale', robotImgGrayscale)

cv2. waitKey(0)
cv2. destroyAllWindows()

cv2.imwrite('./save/img/humanoid_grascale.jpg', robotImgGrayscale)

#불필요한 과정 줄이기
robotImgGrayscale = cv2.imread('./res/img/humanoid.jpg', cv2.IMREAD_GRAYSCALE)
robotImgGrayscale = cv2.resize(robotImgGrayscale, (330, 565))
cv2.imwrite('./save/img/humanoid_grascale.jpg', robotImgGrayscale)
#저장에 성공하면 True, 실패하면 False가 뜬다. 해당 디렉토리를 못 찾으면 False가 뜨는듯하다.
'''

##동영상 복사 저장
robotMOV = cv2.VideoCapture('./res/mov/humanoid.mp4') #파일 읽기

#코덱 정의
# cv2.VideoWriter_fourcc('D', 'I', 'V', 'X' ) #()안에 코덱값을 넣는다.
fourcc =cv2.VideoWriter_fourcc(*'DIVX' ) # ='D', 'I', 'V', 'X'

width = int(robotMOV.get(cv2. CAP_PROP_FRAME_WIDTH))
height = int(robotMOV.get(cv2. CAP_PROP_FRAME_HEIGHT))

fps = robotMOV.get(cv2.CAP_PROP_FPS)

robotMovOutput = cv2.VideoWriter('./save/mov/robotMov-output.mp4', fourcc, fps, (width, height))

while robotMOV.isOpened():
    result, frame = robotMOV.read()
    if not result:
        print('MOVIE END')
        break
    
    robotMovOutput.write(frame)
    
    frame = cv2.resize(frame, (330, 565))
    cv2.imshow('title-robotMOV', frame)

    if cv2.waitKey(1) == ord('q'):
        print('MOVIE END')
        break

robotMOV.release()
cv2.destroyAllWindows()