class People:
    eyes = 2
    noses = 1
    mouths = 1
    hands = 2
    legs = 2
    foot = 2


def init():
    jaeHoon = People()
    print("재훈이 눈 개수 :", jaeHoon.eyes)
    print("재훈이 코 개수 :", jaeHoon.noses)
    print("재훈이 입 개수 :", jaeHoon.mouths)

    jaeHoon.heads = 1
    print("재훈이 머리 개수 :", jaeHoon.heads)


init()