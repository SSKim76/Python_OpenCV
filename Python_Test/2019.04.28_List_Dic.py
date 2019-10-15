Python 3.7.3 (default, Mar 28 2019, 10:38:38) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("JoinST INC\n" * 100)
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC
JoinST INC

>>> interest = ['삼성전자', 'LG전자', '네이버']
>>> interrest
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    interrest
NameError: name 'interrest' is not defined
>>> interest
['삼성전자', 'LG전자', '네이버']
>>> print(interest)
['삼성전자', 'LG전자', '네이버']
>>> print(interest[0])
삼성전자
>>> daishin = [9130, 9150, 9150, 9300, 9400]
>>> daishin
[9130, 9150, 9150, 9300, 9400]
>>> daishin[2]
9150
>>> mystock = ['Naver', 5000]
>>> mystock
['Naver', 5000]
>>> kospi_top10 = ['삼성전자', 'SK하이닉스', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER', '현대모비스']
>>> print('시가총액 5위 : ', kospi_top10[4])
시가총액 5위 :  아모레퍼시픽
>>> print(kospi_top10[0:5])
['삼성전자', 'SK하이닉스', '현대차', '한국전력', '아모레퍼시픽']
>>> kospi_top10.append('SK텔레콤')
>>> kospi_top10
['삼성전자', 'SK하이닉스', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER', '현대모비스', 'SK텔레콤']
>>> kospi_top10.insert(2, 'LG전자')
>>> kospi_top10
['삼성전자', 'SK하이닉스', 'LG전자', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER', '현대모비스', 'SK텔레콤']
>>> len(kospi_top10)
12
>>> del kospi_top10[-2]
>>> kospi_top10
['삼성전자', 'SK하이닉스', 'LG전자', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER', 'SK텔레콤']
>>> del kospi_top10[-1]
>>> kospi_top10
['삼성전자', 'SK하이닉스', 'LG전자', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER']
>>> ['삼성전자', 'SK하이닉스', 'LG전자', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER']
['삼성전자', 'SK하이닉스', 'LG전자', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER']

>>> 
>>> 
>>> t = ('samsung', 'LG', "SK")
>>> t
('samsung', 'LG', 'SK')
>>> len(t)
3
>>> cur_price = {}
>>> type(cur_price)
<class 'dict'>
>>> cur_price['daeshin'] = 3000
>>> cur_price[kospi_top10] = 100000
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    cur_price[kospi_top10] = 100000
TypeError: unhashable type: 'list'
>>> cup_rpice[kospi_top10[0]] = 100000
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    cup_rpice[kospi_top10[0]] = 100000
NameError: name 'cup_rpice' is not defined
>>> cur_price[kospi_top10[0]] = 100000
>>> cur_price
{'daeshin': 3000, '삼성전자': 100000}
>>> cur_price['Daum KAKAO'] = 80000
>>> cup_price
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    cup_price
NameError: name 'cup_price' is not defined
>>> cur_price
{'daeshin': 3000, '삼성전자': 100000, 'Daum KAKAO': 80000}
>>> len(cur_price)
3
>>> 
>>> 
>>> del cur_price[kospi_top10[0]]
>>> cur_price
{'daeshin': 3000, 'Daum KAKAO': 80000}
>>> cur_price_key = cur_price.keys()
>>> cur_price_key
dict_keys(['daeshin', 'Daum KAKAO'])
>>> cur_price_list_key = list(cur_price.keys())
>>> cur_price_list_key
['daeshin', 'Daum KAKAO']
>>> cur_price_value = list(cur_price.value())
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    cur_price_value = list(cur_price.value())
AttributeError: 'dict' object has no attribute 'value'
>>> cur_price_value = list(cur_price.values())
>>> cur_price_value
[3000, 80000]
>>> 'Samsung' in cur_price_list_key
False
>>> 'daeshin' in cur_price_list_key
True
>>> naver_end_price = [474500, 461500, 501000, 500500, 488500]
>>> naver_end = {0907 : 474500, 0908 : 461500, 0909 : 501000, 0910 : 500500, 0911 : 488500}
SyntaxError: invalid token
>>> naver_end = {'0907' : 474500, '0908' : 461500, '0909' : 501000, '0910' : 500500, '0911' : 488500}
>>> print('주간 최대 가격 = ', max(naver_end_price))
주간 최대 가격 =  501000
>>> print('주간 최소 가격 = ', min(naver_end_price))
주간 최소 가격 =  461500
>>> print('주간 최대가 - 최소가 = ', max(naver_end_price) - min(naver_end_price))
주간 최대가 - 최소가 =  39500
>>> print('9월 9일 수요일 종가 = ', naver_end_price[2])
9월 9일 수요일 종가 =  501000
>>> max(naver_end.values)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    max(naver_end.values)
TypeError: 'builtin_function_or_method' object is not iterable
>>> naver_end_values = list(naver_end_price.values)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    naver_end_values = list(naver_end_price.values)
AttributeError: 'list' object has no attribute 'values'
>>> max(naver_end.values())
501000
>>> naver_end_values = list(naver_end_price.values())
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    naver_end_values = list(naver_end_price.values())
AttributeError: 'list' object has no attribute 'values'
>>> naver_end_value = list(naver_end.values())
>>> naver_end_vlaue
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    naver_end_vlaue
NameError: name 'naver_end_vlaue' is not defined
>>> naver_end_value
[474500, 461500, 501000, 500500, 488500]
>>> max(naver_end_vlaue)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    max(naver_end_vlaue)
NameError: name 'naver_end_vlaue' is not defined
>>> max(naver_end_value)
501000
>>> print('9월 9일 목요일 종가 = ', naver_end['0909'])
9월 9일 목요일 종가 =  501000
>>> 
