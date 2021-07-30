# 파이썬 기초

1. Immutable vs Mutable
- Immutable : 변하지 않는 값 → 정수, 실수, 문자열, 튜플
- Mutable : 변하는 값 → 리스트, 딕셔너리, 집합

```python
a = 1 #전역 변수
def vartest(a):
	a = a+1

vartest(a)
print(a)
>> 1 #값의 변화가 없음
```

```python
b = [1,2,3,4]
def vartest2(b):
	b = b.append(5)

vartest2(b)
print(b)
>> [1,2,3,4,5] #값이 변함
```

1. 클래스
- 반복되는 변수 & 함수를 미리 정해놓은 틀(설계도)

```python
r1 = 0
r2 = 0

def add1(num):
	global r1
	r1 += num
	return r1

def add2(num):
	global r2
	r2 += num
	return r2

print(add1(3))
print(add1(4))

print(add2(3))
print(add3(7))

>> 3
>> 7
>> 3
>> 10
```

```python
#클래스 함수로 생성
class calculator:     #calculator 클래스
	def __init__(self): #초기값을 설정
		self.result = 0   #result = 0

	def add(self, num):
		self.result += num
		return self.result

cal1 = calculator() #cal1은 calculator로 만든 객체(인스턴스)
cal2 = calculator()

print(cal1.add(3)) #cal클래스의 add함수를 사용
print(cal1.add(4))
print(cal2.add(5))
print(cal2.add(7))
```

```python
class cal:
	def setdata(self, first, second): #클래스안의 함수 setdata는 메소드
		self.first = first
		self.second = second

a = cal() #객체, 인스턴스
a.setdata(1,2) #a-self, 1-frist, 2-second
```

```python
class cal:
	def setdata(self, first, second): #클래스안의 함수 setdata는 메소드
		self.first = first
		self.second = second

	def add(self):
		result = self.first + self.second
		return result

a = cal() #객체, 인스턴스
a.setdata(1,2)
print(a.add()) 
>> 3
```

```python
class cal:
	def __init__(self, first,second): #맨 처음 시행
		self.first = first
		self.second = second
	def setdata(self, first, second): #클래스안의 함수 setdata는 메소드
		self.first = first
		self.second = second

	def add(self):
		result = self.first + self.second
		return result

a = cal() #객체, 인스턴스
a.setdata(1,2)
print(a.add()) 
>> 3
```

- 클래스의 상속

![%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20948f7d2156584c828707e4f5a057cbdf/Untitled.png](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20948f7d2156584c828707e4f5a057cbdf/Untitled.png)

```python
class cal: #부모 클래스

	first = 2 #클래스 변수
	second = 3

	def __init__(self, first,second): #객체 변수
		self.first = first
		self.second = second
	def setdata(self, first, second):
		self.first = first
		self.second = second

	def add(self):
		result = self.first + self.second
		return result

#자식 클래스
class morecal(cal):
	def pow(self):
		r = self.first ** self.second
		return r

a = morecal(4,2)
print(a.add())
>> 6
print(a.pow())
```

- 오버라이딩 : 자식클래스에서 부모클래스의 함수를 변경 가능

![%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20948f7d2156584c828707e4f5a057cbdf/Untitled%201.png](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20948f7d2156584c828707e4f5a057cbdf/Untitled%201.png)

1. 모듈, 패키지
- 함수, 변수, 클래스를 미리 만들어놓은 .py파일

```python
import mod1
print(mod1.add(1,2))

from mod1 import add
```

```python
def add(a,b):
	return a+b

def sub(a,b):
	return a-b

if __name__ == "__main__" #name이 main인 경우만 실행
	print(add(1,4))
	print(add(2,3))
```

```python
import sys
sys.path.append('경로지정')
import mod1

print(mod1.add(3,4))
```

- 패키지 : 모듈을 여러 개 모아둔 것

![%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20948f7d2156584c828707e4f5a057cbdf/Untitled%202.png](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20948f7d2156584c828707e4f5a057cbdf/Untitled%202.png)

```python
#패키지.폴더.모듈.함수()
import game.sound.echo
game.sound.echo.echo_test()

from game.sound import echo
echo.echo_test()

from game.sound.echo import echo_test as e
e()

from game.sound import * #__init__.py에 무엇을 가져올 것인지 기록
echo.echo_test()
```

1. 예외 처리
- 오류가 발생했을 때 어떻게 할지 정하는 것

![%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20948f7d2156584c828707e4f5a057cbdf/Untitled%203.png](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%20%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20948f7d2156584c828707e4f5a057cbdf/Untitled%203.png)

```python
try:
	4/0
except Exception as e: #오류발생 시 실행
	print(e)
else:
 pass    #try가 성공하면 실행됨
finally:
	pass   #무조건 마지막에 실행
```

1. 내장함수, 외장함수
- 내장 함수 : 파이썬에 내장된 함수

```python
#filter 함수
def positive(x):
	return x > 0

a = list(filter(positive,[1,-3,2,0,-5,6]))
print(a)

>> [1,2,6]
```

```python
#map 함수
a = list(map(lambda x : x*2, [1,2,3,4]))
print(a)

>> [2,4,6,8]
```

```python
#zip 함수
list(zip([1,2,3],[4,5,6]))
>> [(1,4),(2,5),(3,6)]
```

- 외장 함수 : 라이브러리 함수, import 해서 쓰는 것
