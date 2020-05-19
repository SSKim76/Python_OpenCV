import cv2
import numpy as np
import matplotlib.pyplot as plt


def showImage():
    imgfile = 'img/100.jpg'

    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
    img_gray = cv2.imread(imgfile, 0) # GrayScale
    img_alp = cv2.imread(imgfile, cv2.IMREAD_UNCHANGED)

    cv2.imshow('Kyung Hyun', img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    cv2.imshow('Kyung Hyun - GrayScale', img_gray)
    cv2.waitKey(1500)
    cv2.destroyAllWindows()

    cv2.imshow('Kyung Hyun - Unchanged', img_alp)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

    # Window Size 변경 가능
    cv2.namedWindow('Kyung Hyun - NORMAL', cv2.WINDOW_NORMAL)
    cv2.imshow('Kyung Hyun - NORMAL', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Image 복사
    k = cv2.waitKey(0) & 0xFF

    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('c'):
        cv2.imwrite("img/100_copy.jpg", img)
        cv2.destroyAllWindows()

    #Matplotlib 사용하기(비율맞춰 Size변경, 저장 등 네비게이션)
    img_gray = cv2.imread(imgfile, 0)  # GrayScale
    plt.imshow(img_gray, cmap = 'gray', interpolation='bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.title('Kyung Hyun')
    plt.show()


showImage()



