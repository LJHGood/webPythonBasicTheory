def testFunction(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)

def init():
    print("튜플 인자 0개")
    testFunction()
    print()

    print("튜플 인자 5개")
    testFunction(1, 2, 3, 4, 5)
    print()

    print("딕셔너리 인자 5개")
    testFunction(b = 1, c = 2)
    print()

    print("딕셔너리와 튜플 인자 여러개 예시")
    testFunction(5, 3, 5, "Aa", "w", b = 1, c = 2)

init()