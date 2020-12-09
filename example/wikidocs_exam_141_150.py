# https://wikidocs.net/7014

# 141
sell_price = [100, 200, 300]
for i in sell_price:
    print(i+10)
print()

# 142
food_list = ['김밥', '라면', '튀김']
for i in food_list:
    print('오늘의 메뉴: ', i)
print()

# 143
stock_list = ['sk', 'SAMSUNG', 'LG']
for i in stock_list:
    print(len(i))
print()

# 144
animal_list = ['dog', 'cat', 'parrot']
for i in animal_list:
    print(i, len(i))
print()

# 145
animal_list = ['dog', 'cat', 'parrot']
for i in animal_list:
    print(i[:1])
print()

# 146
nums = [1, 2, 3]
for i in nums:
    print(f'3 x {i}')
print()

# 147
nums = [1, 2, 3]
for i in nums:
    print(f'3 X {i} = ', 3*i)
print()

# 148
list_korea_words = ['가', '나', '다', '라']
for i in list_korea_words[1:]:
    print(i)
print()

# 149
list_korea_words = ['가', '나', '다', '라']
for i in list_korea_words[::2]:
    print(i)
print()

# 150
list_korea_words = ['가', '나', '다', '라']
for i in list_korea_words[::-1]:
    print(i)
