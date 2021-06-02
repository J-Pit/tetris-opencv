import cv2


# displays output from computers webcam
# press s to save image for tetris game
# press q to quit

def cam():
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow("img", img)
        key = cv2.waitKey(1)
        if key == ord('s'):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (7, 7), 0)
            th, im_th = cv2.threshold(blur, 80, 255, cv2.THRESH_BINARY)
            cv2.imwrite("temp.png", im_th)
        elif key == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()




cam()
