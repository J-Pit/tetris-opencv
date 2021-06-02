# takes an image and returns a 2D array based of image to use in a tetris game

import cv2
import random


def imgToTetris(img):
    colours = ['1', '2', '3', '4', '5', '6', '7']
    r = random.choice(colours)
    img = cv2.imread(img, 0)

    # print(img.shape)

    width = 5
    height = 5
    dim = (width, height)

    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    def setupMapping():
        characterSet = list((r * 18) + '00000000')
        for i in range(26):
            for j in range(10):
                num[i * 10 + j] = characterSet[i]

    num = {}
    setupMapping()
    # print(num)
    transformed = []
    matrix = []
    for i in img:

        temp = []
        for j in i:
            temp.append(num[j])
        transformed.append(temp)

    for i in transformed:
        matrix.append(list(map(int, i)))
    for i in range(4):
        matrix = [x for x in matrix if int(r) in x]
        matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]

    for i in matrix:
        print(i)

    return matrix


