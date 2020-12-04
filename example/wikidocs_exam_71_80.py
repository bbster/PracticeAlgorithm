# https://wikidocs.net/7014

# 071
my_variable = ()
print(my_variable, type(my_variable))
print()

# 072
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank, type(movie_rank))
print()

# 073
num = (1,)
print(num, type(num))
print()

# 하나의 정수값을 저장하면 튜플이 아닌 정수로 인식함
# 하나의 데이터가 저장되는 경우 뒤에 쉼표를 붙여주도록 하자.

# 074
# t = (1, 2, 3)
# t[0] = 'a'
print()
# 튜플의 원소의 값은 변경 할수가 없음

# 075
t = 1, 2, 3, 4
print(type(t))
print()

# 원칙적으로 튜플은 괄호와 함께 데이터 정의를 해야하지만
# 사용자 편의를 위해 괄호 없이도 동작.

# 076
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)
print()

# 튜플의 엘리먼트는 수정할수 없기 때문에
# 값을 변경 하기 위해서 새로운 튜플을 만들어서 변수를 업데이트를 해줘야함

# 077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(interest, type(interest))
interest = list(interest)
print(interest, type(interest))
print()

# 078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(interest, type(interest))
interest = tuple(interest)
print(interest, type(interest))
print()

# 079
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 080
even_nums = tuple(range(2, 100, 2))
print(even_nums)
