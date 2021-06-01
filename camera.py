import cv2


def cam():
    key = cv2.waitKey(1)
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow("img", img)
        key = cv2.waitKey(1)
        if key == ord('s'):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (7, 7), 0)
            th, im_th = cv2.threshold(blur, 80, 255, cv2.THRESH_BINARY)
            cv2.imwrite("opencv.png", im_th)

    cap.release()

    print(blur)



cam()
