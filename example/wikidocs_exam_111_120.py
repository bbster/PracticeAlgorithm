# https://wikidocs.net/7014

# 111
hi = input("입력: ")
print(hi*2)

# 112
num = int(input('숫자를 입력하세요:'))
print(num+10)

# 113
num = int(input('숫자를 입력하세요:'))
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')

# 114
num = int(input('숫자를 입력하세요:'))
num = num + 20
if num < 255:
    print(num)
else:
    print(255)

# 115
# 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 출력 값의 범위는 0~255이다.
# 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
num = int(input('숫자를 입력하세요:'))
num = num - 20
if num < 0:
    print(0)
elif num > 255:
    print(255)
else:
    print(num)

# 116
time = input("현재시간: ")
if time[-2:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")

# 117
fruit = ["사과", "포도", "홍시"]
answer = input('좋아하는 과일은?')

if answer in fruit:
    print('정답입니다.')
else:
    print('오답입니다')

# 118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user_investment = input('투자 종목을 입력해주세요: ')
if user_investment in warn_investment_list:
    print('투자 경고 종목입니다.')
else:
    print('투자 경고 종목이 아닙니다.')

# 119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user_favorite_weather = input('제가 좋아하는 계절은: ')
if user_favorite_weather in fruit.keys():
    print('정답입니다.')
else:
    print('오답입니다.')

# 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user_favorite_weather = input('제가 좋아하는 계절은: ')
if user_favorite_weather in fruit.values():
    print('정답입니다.')
else:
    print('오답입니다.')
