
import cv2 as cv2

def select_img(sel_num):
    return{
        0 : 'img/100.jpg',                 # 경현
        1 : 'img/images_1.jpg',          # 그라데이션 이미지
        2 : 'img/multi_light.jpg',          #
        3 : 'img/opencv_logo.jpg',
        4 : 'img/sample_img1.jpg',       # 산과 강이 있는 풍경
        5 : 'img/sample_img2.jpg',       # 수지 이미지
        6 : 'img/sdoku.jpg',                  #
        7 : 'img/tile.jpg',                     # Threshold Test용 타일
        8 : 'img/girl.png',                      # 기본여자 이미지
        9 : 'img/alpha1.jpg',                    # 알파벳 및 숫자 이미지
        10: 'img/noise_alp.jpg'
    }.get(sel_num,'img/girl.png')


def close_window():
    cv2.waitKey(0)
    cv2.destroyAllWindows( )