import numpy as np
import  cv2
from random import shuffle  # shuffle() 함수 사용을 위해
import math # sqrt 함수 사용을 위해, sqrt(x) -> 루트 x , 제곱근을 구하는 함수

mode, drawing = True, False
ix, iy = -1, -1
# 색상값을 위해 사용될 0~255를 멤버로 하는 리스트 생성
b = [i for i in range(256)]
g = [i for i in range(256)]
r = [i for i in range(256)]

#   마우스 이벤트를 처리할 콜백 함수
#   cv2.setMouseCallBack()함수의 인자로 지정되어 호출
#   event : 마우스 이벤트
#   x, y: 마우스 이벤트가 일어난 위치
#   flags: 여기서는 사용하지 않음
#   param: cv2.setMouseCallback() 함수에서 전달받은 사용자 데이터


def onMouse(event, x, y, flags, param):
    global ix, iy, drawing, mode, b, g, r

    if event == cv2.EVENT_LBUTTONDBLCLK:
        #   마우스 왼쪽 버튼으로 더블클릭할때 발생
        shuffle(b), shuffle(g), shuffle(r)
        cv2.circle(param, (x,y), 50, (b[0], g[0], r[0]),  -1)

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        shuffle(r), shuffle(g), shuffle(b)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(param, (ix,iy), (x,y), (b[0], g[0], r[0]), -1)
            else :
                rx = (ix-x)**2 + (iy-y)**2
                rx = int(math.sqrt(rx))
                cv2.circle(param, (ix, iy), rx, (b[0], g[0], r[0]), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(param, (ix, iy), (x, y), (b[0], g[0], r[0]), -1)
        else:
            rx = (ix - x)**2 + (iy-y)**2
            rx = int(math.sqrt(rx))
            cv2.circle(param, (ix, iy), rx, (b[0], g[0], r[0]), -1)




def mouseBrush():

    global mode

    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('paint')
    cv2.setMouseCallback('paint', onMouse, param = img)


    while True:
        cv2.imshow('paint', img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27 :
            break
        elif k == ord('m') :
            mode = not(mode)
            # 모드 변경 직사각형 -> 원 또는 원 -> 직사각형


    cv2.destroyAllWindows()

mouseBrush()

