import cv2
def cam():
    cap=cv2.VideoCapture(0)

    ret, img=cap.read()
    cap.release()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    print(blur)
    th, im_th = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)
    cv2.imwrite("opencv.png", im_th)



