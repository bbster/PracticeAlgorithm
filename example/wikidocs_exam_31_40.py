# https://wikidocs.net/7014

# 031
a = "3"
b = "4"
print(a + b)
print(" ")

# 032
print("Hi" * 3)
print(" ")

# 033
print("-" * 80)
print(" ")

# 034
t1 = 'python'
t2 = 'java'
print((t1 + t2) * 4)
print(" ")

# 답안지
# t1 = "python"
# t2 = "java"
# t3 = t1 + ' ' + t2 + ' '
# print(t3 * 4)

# 035 use % formatting
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print('이름: %s 나이: %d' %(name1, age1))
print('이름: %s 나이: %d' %(name2, age2))
print(" ")

# 036 use format() method
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print('이름: {} 나이: {}'.format(name1, age1))
print('이름: {} 나이: {}'.format(name2, age2))
print(" ")

# 037 use f-string
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')
print(" ")

# 038
상장주식수 = "5,969,782,550"
상장주식수 = int(상장주식수.replace(",", ''))
print(상장주식수, type(상장주식수))
print(" ")

# 039
분기 = "2020/03(E) (IFRS연결)"
분기 = 분기.split("(")
print(분기[0])
# 답안지
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])
print("")

# 040
data = "   삼성전자    "
data = data.replace(" ", '')
print(data)

# 답안지
# data = "   삼성전자    "
# data1 = data.strip()
# print(data1)
# strip()은 문자열 메서드이며 주어진 문자열 양쪽끝에 있는 공백과 \n 기호를 삭제시켜준다.
