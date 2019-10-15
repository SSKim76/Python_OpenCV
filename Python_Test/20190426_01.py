Python 3.7.3 (default, Mar 28 2019, 10:38:38) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World")
Hello World
>>> print(hello)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(hello)
NameError: name 'hello' is not defined
>>> 
>>> 
>>> print(2+3)
5
>>> print('안녕하세요.')
안녕하세요.
>>> 
>>> 
>>> print('주식은 대박이다.')
주식은 대박이다.
>>> print("I love 'you'")
I love 'you'
>>> print("I like you')
      
SyntaxError: EOL while scanning string literal
>>> print('korea')
korea
>>> print{Hello}
SyntaxError: invalid syntax
>>> print['hello']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print['hello']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> 
>>> 
>>> 
>>> 601000*10
6010000
>>> 601000 * 10
6010000
>>> 601000 * 0.97
582970.0
>>> 601000 - 587000
14000
>>> 180 * 10 + 10000
11800
>>> naver = 601000
>>> naver
601000
>>> print(naver)
601000
>>> naver * 10
6010000
>>> 
>>> 
>>> 
>>> 
>>> naver
601000
>>> id(naver)
43221600
>>> x = 100
>>> y = 100
>>> id(x) ,id(y)
(262262480, 262262480)
>>> x = 10000
>>> y = 10000
>>> id(x), id(y)
(43224912, 43224960)
>>> c = 100000
>>> t = 100000
>>> id(c), id(t)
(43224944, 43225056)
>>> 
>>> 
>>> 
>>> mystring = 'hello world'
>>> mystring1 = 'a'
>>> mystring2 = "a"
>>> mystring3 = "abc mart"
>>> mystring
'hello world'
>>> print(mystring)
hello world
>>> len(mystring), len(mystring1)
(11, 1)
>>> mystring[0:5]
'hello'
>>> print(mystring[0:5])
hello
>>> print(mystring[6:11])
world
>>> print(mystring[0:])
hello world
>>> print(mystring[0:-2])
hello wor
>>> my_jusik = "naver daum"
>>> c
100000
>>> my_jusic
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    my_jusic
NameError: name 'my_jusic' is not defined
>>> my_jusik
'naver daum'
>>> my_jusik.split(' ')
['naver', 'daum']
>>> my_jusik.split(' ')[0], my_jusik.split(' ')[1]
('naver', 'daum')
>>> my_jusik.split(' ')[0]
'naver'
>>> split_jusik = my_jusik.split(' ')
>>> print(split_jusik[1])
daum
>>> price_Daum = 89000
>>> price_Naver = 751000
>>> Qty_Daum = 100
>>> Qty_Naver = 20
>>> print('Total Price = ' price_Daum * Qty_Daum + price_Naver * Qty_naver)
SyntaxError: invalid syntax
>>> print('Total Price = ' + price_Daum * Qty_Daum + price_Naver * Qty_naver)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print('Total Price = ' + price_Daum * Qty_Daum + price_Naver * Qty_naver)
TypeError: can only concatenate str (not "int") to str
>>> Total_Price = price_Daum * Qty_Daum + price_Naver * Qty_naver
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    Total_Price = price_Daum * Qty_Daum + price_Naver * Qty_naver
NameError: name 'Qty_naver' is not defined
>>> 
>>> Total_Price = price_Daum * Qty_Daum + price_Naver * Qty_Naver
>>> print('Total Price = ' + price_Daum * Qty_Daum + price_Naver * Qty_naver)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    print('Total Price = ' + price_Daum * Qty_Daum + price_Naver * Qty_naver)
TypeError: can only concatenate str (not "int") to str
>>> print('Total Price = ' + price_Daum * Qty_Daum + price_Naver * Qty_Naver)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print('Total Price = ' + price_Daum * Qty_Daum + price_Naver * Qty_Naver)
TypeError: can only concatenate str (not "int") to str
>>> print('Total Price = ' + price_Daum * Qty_Daum + price_Naver * Qty_naver)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print('Total Price = ' + price_Daum * Qty_Daum + price_Naver * Qty_naver)
TypeError: can only concatenate str (not "int") to str
>>> print('Total Price = '  price_Daum * Qty_Daum + price_Naver * Qty_naver)
SyntaxError: invalid syntax
>>> print('Total Price = ' , price_Daum * Qty_Daum + price_Naver * Qty_naver)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print('Total Price = ' , price_Daum * Qty_Daum + price_Naver * Qty_naver)
NameError: name 'Qty_naver' is not defined
>>> print('Total Price = ' , price_Daum * Qty_Daum + price_Naver * Qty_Naver)
Total Price =  23920000
>>> Total_Price
23920000
>>> start_Price = 1000000
>>> monday_Price = start_Price * 0.7
>>> tueday_Price = monday_Price * 0.7
>>> wedday_Price = tueday_Price * 0.7
>>> print("수요일의 종가 = ", wedday_Price)
수요일의 종가 =  342999.99999999994
>>> naver_end_Price = price_Naver * 0.9
>>> daum_end_Price = price_Daum * 0.95
>>> print("네이버 손실금액 = ", price_Naver - naver_end_Price)
네이버 손실금액 =  75100.0
>>> print("다음 손실금액 = ", price_Daum - daum_end_Price)
다음 손실금액 =  4450.0
>>>  print("네이버 손실금액 = ", (price_Naver - naver_end_Price)*Qty_Naver)
 
SyntaxError: unexpected indent
>>>  print("네이버 손실금액 = ", (price_Naver - naver_end_Price) * Qty_Naver)
 
SyntaxError: unexpected indent
>>> print("네이버 손실금액 = ", price_Naver - naver_end_Price)
네이버 손실금액 =  75100.0
>>> print("네이버 손실금액 = ", (price_Naver - naver_end_Price) * Qty_Naver)
네이버 손실금액 =  1502000.0
>>> F = 50
>>> C = (F - 32) / 1.8
>>> c
100000
>>> C
10.0
>>> print("Pizza \n" , *10)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    print("Pizza \n" , *10)
TypeError: print() argument after * must be an iterable, not int
>>> print("Pizza \n"  *10)
Pizza 
Pizza 
Pizza 
Pizza 
Pizza 
Pizza 
Pizza 
Pizza 
Pizza 
Pizza 

>>> Name = "파이썬"
>>> Date = "2014년 12월 12일"
>>> P_Num = "20141212-1623210"
>>> print("이름 : ", Name , "생년월일 : ", Date , "주민등록번호 : " , P_Num)
이름 :  파이썬 생년월일 :  2014년 12월 12일 주민등록번호 :  20141212-1623210
>>> s = 'Daum KaKao'
>>> split_s = split(s, ' ')
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    split_s = split(s, ' ')
NameError: name 'split' is not defined
>>> split_f = [0:3]
SyntaxError: invalid syntax
>>> split_f = s[0:3]
>>> split_e = s[5:]
>>> print_str = split_e + ' ' + split_f
>>> print(print_str)
KaKao Dau
>>> split_f = s[0:4]
>>> print_str = split_e + ' ' + split_f
>>> print(print_str)
KaKao Daum
>>> a = 'hello world'
>>> aa = a.split(' ')
>>> aa[0] = 'Hi'
>>> aa
['Hi', 'world']
>>> aa[0]+' '+aa[1]
'Hi world'
>>> 
