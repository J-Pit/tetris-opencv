import cv2


def imgToTetris(img):
    img = cv2.imread(img, 0)
    cap=cv2.VideoCapture(0)


    # print(img)
    # print(img.shape)

    width = 15
    height = 15
    dim = (width, height)
    blur = cv2.GaussianBlur(img, (7, 7), 0)
    th, im_th = cv2.threshold(blur, 220, 255, cv2.THRESH_BINARY);



    im_th = cv2.resize(im_th, dim, interpolation=cv2.INTER_AREA)

    def setupAsciiMapping():
        characterSet = list(('1' * 18) + '00000000')
        for i in range(26):
            for j in range(10):
                asciiToNum[i * 10 + j] = characterSet[i]

    asciiToNum = {}
    setupAsciiMapping()
    # print(asciiToNum)
    transformedAscii = []
    matrix = []
    for i in im_th:
        temp = []
        for j in i:
            temp.append(asciiToNum[j])
        transformedAscii.append(temp)

    for i in transformedAscii:
        matrix.append(list(map(int, i)))
    for i in matrix:
        if 1 not in i:
            matrix.remove(i)

    for row in matrix:
        if row[0] == 0:
            row.pop(0)
        if row[-1] == 0:
            row.pop(-1)
    while True:
        if 1 not in matrix[0]:
            matrix.remove(matrix[0])
        elif 1 not in matrix[-1]:
            matrix.remove(matrix[-1])
        else:
            break

    # make matrix square
    for i in matrix:
        while len(i) > len(matrix):
            i.pop(-1)
        while len(i) < len(matrix):
            i.append(0)


    for row in matrix:
        print(row)



    return matrix


imgToTetris("images/S.png")
