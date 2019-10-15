
import numpy as np
import cv2


#   cv2.line(공간, 시작점, 끝점, BRG값, 두께) : 직선을 그리는 함수
#   cv2.circle(공간, 원의 중심, 반지름, BGR값, -1(주어진색으로 채움) : 원을 그리는 함수
#   cv2.rectangle(공간, 좌측상단, 우측하단, BGR, 두께) : 직사각형을 그리는 함수
#   cv2.ellipse(공간, 중심점, 장축과 단축의 길이, 기울기 각도, 시작각, 끝각) : 타원을 그리는 함수
#   cv2.putText() : 텍스트 입력 함수
#   cv2.?????(그릴공간, 첫번째좌표(X,Y), 두번째좌표(X,Y), Color(xxx,xxx,xxx), 두께)

def drawing():

    img = np.zeros((512, 512, 3), np.uint8)
    #img = np.zeros((512, 512), np.uint8)  # 검정색으로만 나오는 이유는?

    #다양한 색상과 선두께를 가진 도형 그리기
    cv2.line(img, (0,0), (511,511), (255,0,0), 5)
    #파란색의 두께5인 직선. 시작점, 끝점

    cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)
    # 녹색의 두께3인 직사각형.  좌상단 모서리, 우하단 모서리

    cv2.circle(img, (100,100), 100, (0,0,255), -1)
    # 빨간색으로 채운 반지름 100짜리 원. (100, 100) 원의 중심좌표

    cv2.ellipse(img, (256, 256), (100,50), 0,0,180,(255,0,0), -1)
    # 파란색으로 채운 타원, (255,255) : 타원의 중심
    # (100, 50) :  각각 장축과 단축의 1/2 길이
    # 0, 0, 180 : 타원의 기울기 각도, 시작각도, 끝 각도

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,255,255), 2)
    # OpenCV라는 글자를 (10, 50) 위치에 지정된 폰트와 폰트크기, 두께2의 흰색글자자


   cv2.imshow('drawing', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

drawing()
