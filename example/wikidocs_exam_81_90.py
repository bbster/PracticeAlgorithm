# https://wikidocs.net/7014

# 081
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, b, c = tuple(scores) # 튜플로 변활할 이유가 없었따.
print('valid_score:', valid_score, len(valid_score), type(valid_score))
print(b)
print(c)
print()

# 답안지
# *valid_score, _, _ = scores
# print(valid_score)

# 082
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print('valid_score:', valid_score, len(valid_score), type(valid_score))
print()

# 083
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, b = scores
print('valid_score:', valid_score, len(valid_score), type(valid_score))
print()

# 084
# temp 이름의 비어있는 딕셔너리를 만들라.
temp = {}
print(type(temp))
print()

# 085
icecream = {'메로나': 1000, '폴라포': 1200, '빵빠레':1800}
print(icecream, type(icecream))
print()

# 086
icecream = {'메로나': 1000, '폴라포': 1200, '빵빠레':1800}
icecream['죠스바'] = 1200
icecream['월드콘'] = 1500
print(icecream, type(icecream))
print()

# 087
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print('메로나 가격: ', ice.get('메로나'))
print()
# 답안지
# print("메로나 가격: ", ice["메로나"])

# 088
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice.update({'메로나': 1300})
print(ice)
print()
# 답안지
# ice["메로나"] = 1300

# 089
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice.pop('메로나')
print(ice)
print()
# 답안지
# del ice["메로나"]
# print(ice)

# 090
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream['누가바']
# 딕셔너리에 없는키를 사용하여 에러 발생
