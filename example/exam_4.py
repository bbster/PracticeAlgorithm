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


def isInt(a):

    if(type(a) is int):
        return True
    else:
        return False


def isFloat(a):

    if (type(a) is float):
        return True
    else:
        return False


def isStr(a):
    if (type(a) is str):
        return True
    else:
        return False

a=1.1
#a=1
#a='a'

print('-'*60)

print("테스트 값은 " + str(a) + " 입니다")
print('-'*60);

if(isInt(a)):
    print("정수입니다.")

else:
    print("정수가 아닙니다.")

if(isFloat(a)):
    print("실수입니다.")
else:
    print("실수가아닙니다")

if(isStr(a)):
    print("문자열 입니다")
else:
    print("문자열이 아닙니다")