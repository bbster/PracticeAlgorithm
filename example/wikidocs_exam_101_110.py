# https://wikidocs.net/7014

# 101
# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
# boolean

# 102
print('102 :', 3 == 5)
print()
# false

# 103
print('103 :', 3 < 5)
# true
print()

# 104
x = 4
print('104 :', 1 < x < 5)
# true
print()

# 105
print('105 :', (3 == 3) and (4 != 3))
# true and true = true
print()

# 106
#print(3 => 4)
# 부호방식이 잘못됬음 / syntax error
print()

# 107
if 4 < 3:
    print("Hello World")
# 4가 3보다 작을때 프리트문 출력이니까 출력 안함

# 108
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
# 4가 3보다 작을때 위에 프리트문 출력 그외에는 hi there 출력

# 109
if True:
    print ("1")
    print ("2")
else:
    print("3")
print("4")
print()

# 트루일떄 1,2 출력하고 4 출력 그외에는 3출력하고 4인데 트루값이 없으니까 3,4 이지 않을까?
# 근데 1,2,4 가 출력 됨 젠장

# 110
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")

# true 일때 그 다음 값이 false가 아니니까 3 출력하고 5 출력
