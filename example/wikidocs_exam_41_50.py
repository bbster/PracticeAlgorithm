# https://wikidocs.net/7014

# 041
ticker = "btc_krw"
ticker = ticker.upper()
print(ticker)
print("")

# 042
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)
print("")

# 043
a = 'hello world'
print(a)
a = a.capitalize()
b = a.title()
print(a + ' = use capitalize')
print(b + ' = use title')
print("")
# capitalize 메서드는 주어진 문자열에서 첫번째 글자를 대문자로 변환시켜줌
# title 메서드는 주어진 문자열에서 알파벳을 제외한 문자로 나뉘어져 있는 영단어의 첫글자를 대문자로 바꾸어줌

# 044
file_name = "보고서.xlsx"
suffix = 'xlsx'
file_name = file_name.endswith(suffix)
print(file_name)
# 답안지
# file_name = "보고서.xlsx"
# file_name.endswith("xlsx")
print("")

# 045
file_name = "보고서.xlsx"
file_name = file_name.endswith(("xlsx", "xls"))
print(file_name)
# 답안지
# file_name = "보고서.xlsx"
# file_name.endswith("xlsx")
print("")

# 046
file_name = "2020_보고서.xlsx"
file_name = file_name.startswith('2020')
print('Is True? = ', file_name)
print("")

# 047
a = 'hello world'
a = a.split()
print('use split index 0 = ', a[0])
print('use split index 1 = ', a[1])
print("")

# 048
ticker = 'btc_krw'
ticker = ticker.split('_')
print('use split index 0 = ', ticker[0])
print('use split index 1 = ', ticker[1])
print("")

# 049
date = '2020-05-01'
date = date.split('-')
print('use split index 0 = ', date[0] + '년')
print('use split index 1 = ', date[1] + '월')
print('use split index 2 = ', date[2] + '일')
print("")

# 050
data = "039490     "
print(data + "공백")
data = data.rstrip()
print(data + "공백제거")
