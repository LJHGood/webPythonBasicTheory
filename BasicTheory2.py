class People:
    eyes = 2
    noses = 1
    mouths = 1
    hands = 2
    legs = 2
    foot = 2

    # 이건 method
    def setEyes(self, eyes_):
        self.eyes = eyes_
        
# 이건 function
def init():
    jaeHoon = People()
    print("재훈이 눈 개수 :", jaeHoon.eyes)
    print("재훈이 코 개수 :", jaeHoon.noses)
    print("재훈이 입 개수 :", jaeHoon.mouths)

    jaeHoon.heads = 1
    print("재훈이 머리 개수 :", jaeHoon.heads)
    print()
    jaeHoon.setEyes(3)
    print("재훈이 눈 개수 :", jaeHoon.eyes)



# 똑같은 함수인데 클래스 안에 있는건 메서드라 말한다.

init()