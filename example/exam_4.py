def isNumStr(s):

    try:
        int(s)
        return True
    except ValueError:
        return False

    num1 = input("정수를 입력하세요: ")
    num2 = input("다음정수를 입력하세요: ")

    if isNumStr(num1) and isNumStr(num2):
        print(int(num1) - int(num2))
    else:
        print("정수가 아닙니다.")
