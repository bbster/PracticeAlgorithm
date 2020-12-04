# https://wikidocs.net/7014

# 021
letters = 'python'
print(len(letters))
print(letters[0], letters[2])

# 022
license_plate = "24가 2210"
print(license_plate[4:])

# 023
string = "홀짝홀짝홀짝"
print(string[0], string[2], string[4])

# 024
string = 'python'
print(string[::-1])
string_list = list(string)

string_list.reverse()
print(string_list)

# 025
phone_number = '010-1111-2222'
phone_number = phone_number.replace("-", " ")
print(phone_number)
# replace 문자열 인덱스중 특정 문자열 제거가능 
# 위와 같이 -을 제거하고 공백문자를 넣음

# 026
phone_number = '010-1111-2222'
phone_number = phone_number.replace("-", "")
print(phone_number)

# 027
url = "http://sharebook.kr"
print(url[17:])
url_index = url.find("kr")
print(url[url_index:])
url_split = url.split(".")
print(url_split[1])
# split으로 .을 기준으로 잘라낸뒤 두개로 나뉜 인덱스중 원하는 인덱스 출력

# 028
# lang = "python"
# lang[0] = "p"
# print(lang)
# 문자열은 수정할수가 없다. 문자열이 할당 메서드를 지원하지 않기때문

# 029
string = 'abcdfe2a35432a'
string_replace = string.replace("a", "A")
print(string_replace)

# 030
string = 'abcd'
string.repalce('b', 'B')
print(string)
# abcd
# 문자열은 변경할수 없는 자료형이다
# string 변수에 저장되어있는 데이터 자체는 변경되지 않고
# 리턴값을 저장할수 있는 변수값이 따로 필요하다.
# string이라는 문자열은 불가변수 replace한 값을 다시 string에 저장하지 않고서는
# string이라는 변수에 저장된 값을 변하지 않고 그대로 유지된다.
