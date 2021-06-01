import cv2
import random
import numpy as np


def imgToTetris(img):
    col = ['1', '2', '3', '4', '5', '6', '7']
    r = random.choice(col)
    img = cv2.imread(img, 0)

    # print(img.shape)

    width = 5
    height = 5
    dim = (width, height)

    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    print(img)

    def setupAsciiMapping():
        characterSet = list((r * 18) + '00000000')
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

    matrix = [x for x in matrix if int(r) in x]
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]

    matrix = [i for i in matrix if int(r) in i]
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]

    for i in matrix:
        print(i)

    return matrix


imgToTetris("opencv.png")
