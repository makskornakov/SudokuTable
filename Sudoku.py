import random
# begining
m1 = [1,2,3,4,5,6,7,8,9]
m2 = [4,5,6,7,8,9,1,2,3]
m3 = [7,8,9,1,2,3,4,5,6]
m4 = [2,3,4,5,6,7,8,9,1]
m5 = [5,6,7,8,9,1,2,3,4]
m6 = [8,9,1,2,3,4,5,6,7]
m7 = [3,4,5,6,7,8,9,1,2]
m8 = [6,7,8,9,1,2,3,4,5]
m9 = [9,1,2,3,4,5,6,7,8]
# changing
a1 = [0,0,0,0,0,0,0,0,0]
a2 = [0,0,0,0,0,0,0,0,0]
a3 = [0,0,0,0,0,0,0,0,0]
a4 = [0,0,0,0,0,0,0,0,0]
a5 = [0,0,0,0,0,0,0,0,0]
a6 = [0,0,0,0,0,0,0,0,0]
a7 = [0,0,0,0,0,0,0,0,0]
a8 = [0,0,0,0,0,0,0,0,0]
a9 = [0,0,0,0,0,0,0,0,0]
NumA = 0
NumB = 0
def verticalFlip ():
# замена 1 столбца на 3
    for i in range(0,8):
        if i == 0:
            NumA = 0
            NumB = 2
        elif i == 1:
            NumA = 2
            NumB = 0
        elif i == 3:
            NumA = 3
            NumB = 5
        elif i == 4:
            NumA = 5
            NumB = 3
        elif i == 6:
            NumA = 6
            NumB = 8
        elif i == 7:
            NumA = 8
            NumB = 6
        a1[NumA] = m1[NumB]
        a2[NumA] = m2[NumB]
        a3[NumA] = m3[NumB]
        a4[NumA] = m4[NumB]
        a5[NumA] = m5[NumB]
        a6[NumA] = m6[NumB]
        a7[NumA] = m7[NumB]
        a8[NumA] = m8[NumB]
        a9[NumA] = m9[NumB]
# копирование 2 столбца
    for i in range(1, 8):
        if i == 1 or i == 4 or i == 7:
            a1[i] = m1[i]
            a2[i] = m2[i]
            a3[i] = m3[i]
            a4[i] = m4[i]
            a5[i] = m5[i]
            a6[i] = m6[i]
            a7[i] = m7[i]
            a8[i] = m8[i]
            a9[i] = m9[i]
def saveAll():
# копирование из а обратно в м для повторной тосовки
    m1[0:9] = a1[0:9]
    m2[0:9] = a2[0:9]
    m3[0:9] = a3[0:9]
    m4[0:9] = a4[0:9]
    m5[0:9] = a5[0:9]
    m6[0:9] = a6[0:9]
    m7[0:9] = a7[0:9]
    m8[0:9] = a8[0:9]
    m9[0:9] = a9[0:9]
def horisontalFlip():
    a1[0:9] = m3[0:9]
    a3[0:9] = m1[0:9]
    a4[0:9] = m6[0:9]
    a6[0:9] = m4[0:9]
    a7[0:9] = m9[0:9]
    a9[0:9] = m7[0:9]
# копирование без изменений
    a2[0:9] = m2[0:9]
    a5[0:9] = m5[0:9]
    a8[0:9] = m8[0:9]

def saveUnchangedVertiacal(o):
    if o == 0:
            V1 = 6
            V2 = 9
    if o == 1:
            V1 = 0
            V2 = 2

    a1[V1:V2] = m1[V1:V2]
    a2[V1:V2] = m2[V1:V2]
    a3[V1:V2] = m3[V1:V2]
    a4[V1:V2] = m4[V1:V2]
    a5[V1:V2] = m5[V1:V2]
    a6[V1:V2] = m6[V1:V2]
    a7[V1:V2] = m7[V1:V2]
    a8[V1:V2] = m8[V1:V2]
    a9[V1:V2] = m9[V1:V2]





def cubeVerticalFlipA():
    a1[0:2] = m1[3:5]
    a2[0:2] = m2[3:5]
    a3[0:2] = m3[3:5]
    a4[0:2] = m4[3:5]
    a5[0:2] = m5[3:5]
    a6[0:2] = m6[3:5]
    a7[0:2] = m7[3:5]
    a8[0:2] = m8[3:5]
    a9[0:2] = m9[3:5]

    a1[3:5] = m1[0:2]
    a2[3:5] = m2[0:2]
    a3[3:5] = m3[0:2]
    a4[3:5] = m4[0:2]
    a5[3:5] = m5[0:2]
    a6[3:5] = m6[0:2]
    a7[3:5] = m7[0:2]
    a8[3:5] = m8[0:2]
    a9[3:5] = m9[0:2]
# сейвим не измененные
    saveUnchangedVertiacal(0)

def cubeVerticalFlipB():
    a1[3:5] = m1[6:8]
    a2[3:5] = m2[6:8]
    a3[3:5] = m3[6:8]
    a4[3:5] = m4[6:8]
    a5[3:5] = m5[6:8]
    a6[3:5] = m6[6:8]
    a7[3:5] = m7[6:8]
    a8[3:5] = m8[6:8]
    a9[3:5] = m9[6:8]

    a1[6:8] = m1[3:5]
    a2[6:8] = m2[3:5]
    a3[6:8] = m3[3:5]
    a4[6:8] = m4[3:5]
    a5[6:8] = m5[3:5]
    a6[6:8] = m6[3:5]
    a7[6:8] = m7[3:5]
    a8[6:8] = m8[3:5]
    a9[6:8] = m9[3:5]
    # сейвим не измененные
    saveUnchangedVertiacal(1)

def cubeHorisontalFlipA():


    a1[0:9] = m4[0:9]
    a2[0:9] = m5[0:9]
    a3[0:9] = m6[0:9]
    a4[0:9] = m1[0:9]
    a5[0:9] = m2[0:9]
    a6[0:9] = m3[0:9]

    # сейвим 0ли
    a7[0:9] = m7[0:9]
    a8[0:9] = m8[0:9]
    a9[0:9] = m9[0:9]

def cubeHorisontalFlipB():


    a4[0:9] = m7[0:9]
    a5[0:9] = m8[0:9]
    a6[0:9] = m9[0:9]
    a7[0:9] = m4[0:9]
    a8[0:9] = m5[0:9]
    a9[0:9] = m6[0:9]
    # сейвим 0ли
    a1[0:9] = m1[0:9]
    a2[0:9] = m2[0:9]
    a3[0:9] = m3[0:9]


def randomize():
    for i in range(1,20):
        randomChoose = random.randint(1,6)
        print(randomChoose)
        if randomChoose == 1:
            verticalFlip()
            saveAll()
        elif randomChoose == 2:
            horisontalFlip()
            saveAll()
        elif randomChoose == 3:
            cubeVerticalFlipA()
            saveAll()
        elif randomChoose == 4:
            cubeVerticalFlipB()
            saveAll()
        elif randomChoose == 5:
            cubeHorisontalFlipA()
            saveAll()
        elif randomChoose == 6:
            cubeHorisontalFlipB()
            saveAll()

#verticalFlip()

cubeHorisontalFlipB()
saveAll()
randomize()
#cubeVerticalFlipA()
#cubeHorisontalFlipA()

#print(" "+str(m1)+"\n",str(m2)+"\n",str(m3)+"\n",str(m4)+"\n",str(m5)+"\n",str(m6)+"\n",str(m7)+"\n",str(m8)+"\n",str(m9)+"\n")
print(" "+str(a1)+"\n",str(a2)+"\n",str(a3)+"\n",str(a4)+"\n",str(a5)+"\n",str(a6)+"\n",str(a7)+"\n",str(a8)+"\n",str(a9)+"\n")


def remove():
    i = 0
    while i != 54:
        i += 1
        Rstring = random.randint(1,9)
        Rnumber = random.randint(0,8)
        if Rstring == 1:
            if a1[Rnumber] != 0:
                a1[Rnumber] = 0
            else:
                i -= 1
        elif Rstring == 2:
            if a2[Rnumber] != 0:
                a2[Rnumber] = 0
            else:
                i -= 1
        elif Rstring == 3:
            if a3[Rnumber] != 0:
                a3[Rnumber] = 0
            else:
                i -= 1
        elif Rstring == 4:
            if a4[Rnumber] != 0:
                a4[Rnumber] = 0
            else:
                i -= 1
        elif Rstring == 5:
            if a5[Rnumber] != 0:
                a5[Rnumber] = 0
            else:
                i -= 1
        elif Rstring == 6:
            if a6[Rnumber] != 0:
                a6[Rnumber] = 0
            else:
                i -= 1
        elif Rstring == 7:
            if a7[Rnumber] != 0:
                a7[Rnumber] = 0
            else:
                i -= 1
        elif Rstring == 8:
            if a8[Rnumber] != 0:
                a8[Rnumber] = 0
            else:
                i -= 1
        elif Rstring == 9:
            if a9[Rnumber] != 0:
                a9[Rnumber] = 0
            else:
                i -= 1

remove()
print(" "+str(a1)+"\n",str(a2)+"\n",str(a3)+"\n",str(a4)+"\n",str(a5)+"\n",str(a6)+"\n",str(a7)+"\n",str(a8)+"\n",str(a9)+"\n")