class People:

    def __init__(self, *args, **kwargs):
        self.eyes = 2
        self.noses = 1
        self.mouths = 1
        self.hands = 2
        self.legs = 2
        self.foot = 2
        self.contry = kwargs.get("contry", "미국")
        print("사람 객체 생성")
        print(args)
        print(kwargs)

    # 이건 method
    def setEyes(self, eyes_):
        self.eyes = eyes_
        
    def __str__(self):
        # return "하이"
        return f"내 눈 : {self.eyes}개, 코 : {self.noses}개, 입 : {self.mouths}개, 손 : {self.hands}개, 다리 : {self.legs}개, 발 : {self.foot}개, 국가 : {self.contry}"

# 이건 function
def init():
    jaeHoon = People()
    # jaeHoon = People(contry="대한민국")

    print("재훈이 눈 개수 :", jaeHoon.eyes)
    print("재훈이 코 개수 :", jaeHoon.noses)
    print("재훈이 입 개수 :", jaeHoon.mouths)

    jaeHoon.heads = 1
    print("재훈이 머리 개수 :", jaeHoon.heads)
    print()
    jaeHoon.setEyes(3)
    print("재훈이 눈 개수 :", jaeHoon.eyes)

    print(jaeHoon)  # jaeHoon.__str__()이거인데 jaeHoon만 입력해도 __str__() 자동 써진 것
    print(dir(jaeHoon))

    

# 똑같은 함수인데 클래스 안에 있는건 메서드라 말한다.

init()