import cv2

from camera import cam


def imgToTetris(img):
    cam()
    img = cv2.imread(img, 0)

    # print(img.shape)

    width = 20
    height = 20
    dim = (width, height)


    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    print(img)

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
    for i in img:

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


cam()
imgToTetris("opencv.png")
