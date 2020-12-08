# https://wikidocs.net/7014

# 121
user_word = input("한개의 문자를 입력해주세요: ")
if user_word.islower():
    print(user_word.upper())
else:
    print(user_word.lower())

# 122
score = int(input("점수를 입력 해주세요: "))
if 80 < score <= 100:
    print("grade is A")
elif 60 < score <= 80:
    print("grade is B")
elif 40 < score <= 60:
    print("grade is C")
elif 20 < score <= 40:
    print("grade is D")
else:
    print("E")

# 123
# 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라.
# 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
exchange_rate = {'달러': 1167, '엔': 1.096, '유로': 1268, '위안': 171}
user_money = input("입력: ")
money, exchange = user_money.split()
print(float(money) * exchange_rate[exchange], '원')

# 124
num1 = input('input number1: ')
num2 = input('input number2: ')
num3 = input('input number3: ')
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num3 and num2 > num1:
    print(num2)
else:
    print(num3)

# 125
mobile_network_operator = {'011': 'SKT',
                           '016': 'KT',
                           '019': 'LGU+',
                           '010': '알수없음'
                           }
user_phone_number = input("번호를 입력해주세요: ")
what = user_phone_number.split('-')
print('당신은', mobile_network_operator[what[0]], '사용자 입니다')

# 답안지
number = input("휴대전화 번호 입력: ")
num = number.split("-")[0]
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")

# 126
zip_code = {'011': '강북구',
            '012': '강북구',
            '013': '도봉구',
            '014': '도봉구',
            '015': '도봉구',
            '016': '노원구',
            '017': '노원구',
            '018': '노원구',
            '019': '노원구'
            }
user_zip_code = input('우편변호: ')
what = user_zip_code[:3]
# print(what)
print(zip_code[what])

# 127
user_resident_registration_number = input("주민등록번호 입력: ")
slice_number = user_resident_registration_number.split('-')
# print(slice_number)
division_sex = slice_number[1][:1]
# print(division_sex)

# 128
regex = [2, 3, 4, 5, 6, 7]
regex2 = [8, 9, 2, 3, 4, 5]
user_resident_registration_number = input("주민등록번호 입력: ")
slice_number = user_resident_registration_number.split('-')

slice_number_front = list(map(int, slice_number[0]))
slice_number_end = list(map(int, slice_number[1]))

front_number_calc = [slice_number_front[0] * regex[0],
                     slice_number_front[1] * regex[1],
                     slice_number_front[2] * regex[2],
                     slice_number_front[3] * regex[3],
                     slice_number_front[4] * regex[4],
                     slice_number_front[5] * regex[5]]
end_number_calc = [slice_number_end[0] * regex2[0],
                   slice_number_end[1] * regex2[1],
                   slice_number_end[2] * regex2[2],
                   slice_number_end[3] * regex2[3],
                   slice_number_end[4] * regex2[4],
                   slice_number_end[5] * regex2[5]]

calc_check = 11 - (sum(front_number_calc) + sum(end_number_calc)) % 11
if calc_check == slice_number_end[6]:
    print('유효한 주민등록 번호입니다.', calc_check)
else:
    print('유효하지 않은 주민등록 번호입니다.')

# zip이라는 함수를 이용 / 파이썬 리스트 컴프리헨션
print('slice_number_front : ', slice_number_front)
print('slice_number_end : ', slice_number_end)
print('regex1: ', regex)
print('regex2: ', regex2)
products = [num1 * num2 for num1, num2 in zip(slice_number_front, regex)]
print('products: ', products)
products2 = [num1 * num2 for num1, num2 in zip(slice_number_end, regex2)]
print('products2: ', products2)

print(11 - ((sum(products) + sum(products2)) % 11))

# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# 최고가 최저가 차이는 변동폭 / 시가 + 변동폭
# print('최고가', btc.keys('max_price'), '최저가', btc.keys('min_price'))
check_btc = (int(btc['max_price']) - int(btc['min_price'])) + int(btc['opening_price'])
print(check_btc, type(check_btc))
# 시가 + 변동폭이 최고가보다 높을경우 상승장, 낮을경우 하락장
if check_btc > int(btc['max_price']):
    print('상승장')
else:
    print('하락장')
