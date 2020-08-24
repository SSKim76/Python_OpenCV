import numpy as np
import cv2


def showVideo():
    try:
        print('카메라를 구동합니다.')

        # 어떤 카메라를 지정할 지, 1개뿐이면 0으로
        # 저정되어 있는 비디오파일을 재생하려면 경로와 이름지정
        # cap = cv2.VideoCapture('video.mp4')
        cap = cv2.VideoCapture(0)
    except:
        print('카메라 구동실패!!')
        return

    videoWidth = 320
    videoHeight = 240
    cap.set(3, videoWidth)     #해상도 설정
    cap.set(4,videoHeight)

    fps = 24.0      # 저장프레임 설정
    width = int(cap.get(3))
    height = int(cap.get(4))
    fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')

    #out = cv2.VideoWriter('cam_test.avi', fcc, fps, (width, height))
    out = cv2.VideoWriter('cam_Test1.avi', fcc, fps, (320, 240))
    print('녹화를 시작합니다.')



    # 무한루프
    while True:

        ret, frame = cap.read()
        # cap.read() -> 재생되는 비디오를 한 프레임씩 읽는다.
        # 제대로 읽었다면 ret 값은 true
        #frame에 읽은 프레임이 저장

        if not ret:
            print('비디오 읽기 오류')
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #흑백으로 변환환
        #cv2.imshow('video', gray)    #흑백으로 변환한 이미지를 화면에 출력
        cv2.imshow('video', frame)  #프레임을 화면에 출력
        out.write(frame)                #프레임을 저장(cam_test.avi)


        k=cv2.waitKey(1) & 0xFF
        if k ==27:
            print('녹화를 종료합니다')
            break

    cap.release()                       # 오픈한 객체를 해제
    out.release()                       #
    cv2.destroyAllWindows()     # 생성한 모든 윈도우 제거

showVideo()



