#if문 실습
"""
score = int(input("안뇽하세용~~점수입력해주세용: "))

if score >= 80 and score <= 100 :
    print("합격입니당~~~축하드려용")
elif score >= 60 and score <= 79 :
    print("보류입니다~~조금만~기다려~~")
elif score >= 0 and score <= 59:
    print("탈락입니다.그렇게 됐따,,,,,,,,,")
else :
    print("잚못 입력했어용")
"""

# switch문 실습
"""
status = 404

match status :
    case 404:
        print("잘못된 URL")
    case 200:
        print("ok")
    case _:
        print("etc")

"""

# while 실습
"""
n = 1
while n <= 10:
    print(n, end = ' ')
    n = n + 1
"""

# while 실습(2)
"""
import time
while True:
    print("빨강")
    time.sleep(1)
    print("파랑")
    time.sleep(1)
    print("초록")
    time.sleep(1)

"""

#2025년까지 윤년 개수 구하기
"""
year = 1
count = 0
while year <= 2025:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        count = count + 1
    year = year + 1

print("2025년까지 윤년의 개수 :", count)

"""

# while - else
"""
n = 1
while n < 11: // 이렇게 쓰는게 n <=10 보다 어떤 숫자에서 끝나는지(11) 이해하기 쉬움.
    print(n)
    n = n+1
else:
    print("완료")
"""


# for문
"""
games = ["LoL", "배틀그라운드", "하스스톤"]
for game in games:
    print(game)

for i in range(10):
    print(i)
"""

# builtin 함수 확인
"""
print(dir(__builtins__))
"""

"""
def addIntegerwithInteger(first:int, second:int) -> tuple:
    result1 = first + second
    result2 = first - second
    return (result1, result2)

print(addIntegerwithInteger(5, 30))
"""

#매개변수
"""
def CallByValue(a : int) -> None :
    print(a)
    a = a + 1
    print(a)

x = 10
CallByValue(x)
print(x)
"""

#매개변수 기본값
"""
def sub(first:int, second:int = 0) -> int:
    return first - second

print(sub(*{100,200}))
"""

# 가변 매개변수
"""
def tot(*args : int) -> int:
    result = 0
    for arg in args:
        result = result + arg
    
    return result

print(tot(10,20))
"""
# 피보나치 수열 - 순회
"""
def fibonacci1(num:int) -> int:
    first = 1
    second = 1
    result 

    for i in range()
    return result 

fibonacci1(10)
fibonacci1(100)
"""

# 피보나치 수열 - 재귀
"""
def fibonacci2(num:int) -> int:
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else :
        return fibonacci2(num-1)+fibonacci2(num-2)

print(fibonacci2(10))
print(fibonacci2(100))

"""
# decorator
# 여기에 common concern 내용
def deco(f): #f 자리에는 아무거나 써줘도 됨. 보통 func로 많이 씀.
    def inner():
        print("실제 수행할 함수")
    return inner

@deco
# 이 안에 business logic 내용
def target():
    print("running target")

target()



# 2부터 1000까지 소수의 개수 구하기 -> 실습해보기

# 2부터 1000까지 완전수(자신을 제외한 약수의 합이 자신과 같은 수) -> 실습해보기
# 6: 1,2,3,6

# 피보나치 수열 해보기 - 순회

# 별찍기
"""
바깥쪽 i를 줄의 개수
안쪽 j를 각 줄의 개수 -> j를 i에 관한 식으로 나타낼텐데 다음 줄로 갈수록 별 개수 증가 -> +i, 다음 줄로 갈수록 별 개수 감소 -> -i
수정을 최소한으로 한다!
  *
 ***
******
 ***
  *
이거 해보기
"""
