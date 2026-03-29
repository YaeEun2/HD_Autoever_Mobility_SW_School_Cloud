# if문 실습
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

n = 0
while True:
    match n % 3:
        case 0:
            print("Red")
        case 1:
            print("Blue")
        case 2:
            print("Green")
    n = n + 1
    time.sleep(1)

"""

# 1년부터 2025년까지 윤년 개수 구하기
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

# 구구단 전체 출력 - for 문
""" 
for i in range (1, 10):
    for j in range (2, 10):
        print("%d * %d = %d" %(j, i, i * j), end = '\t')
    print()
"""

# * 출력(1) - *을 5개씩 5개 출력 : 틀
"""
for i in range(5):
    for j in range(5):
        print('*', end = '')
    print()

"""
# 결과
"""
*****
*****
*****
*****
*****
"""

# * 출력(2) - *을 1 -> 2 -> 3 -> 4 -> 5개 출력
"""
for i in range(5):
    for j in range(i+1):
        print('*', end = '')
    print()

"""
# 결과
"""
*
**
***
****
*****
"""

# * 출력(3) - *을 1 -> 3 -> 5 -> 7 -> 9개 출력(좌우대칭)
"""
for i in range(5):
    for j in range(0, 5-i):
        print(' ', end='')
    for j in range(0, 2*i+1):
        print('*', end = '')
    print()

"""
# 결과
"""
     *
    ***
   *****
  *******
 *********
"""

# * 출력(4) - 다이아몬드 모양 (1 -> 3 -> 5 -> 3 -> 1)출력
"""
for i in range(5):
    # 증가 구간
    if i <= 2:
        for j in range(2-i):
            print(' ', end = '')
        for j in range(0, 2*i+1):
            print('*', end = '')
        print()
    else:
        for j in range(i-2):
            print(' ', end = '')
        for j in range(0, -2*i+9):
            print('*', end = '')
        print()
"""

# 결과
"""
  *
 ***
*****
 ***
  *
"""

# 1부터 100까지 짝수의 합 구하기
"""
sum = 0
for i in range(0, 101, 2):
    sum += i
print(sum)
"""

# 교통 카드 잔액 출력
"""
n = input("인원 수 : ")
balance = 10000

for i in range(int(n)):
    balance -= 1350
    if balance <= 0:
        print("잔액이 부족합니다.")
        break
    else:
        print("교통카드 잔액 : ", balance)

"""

# 2부터 1000까지 소수의 개수 구하기
# Prime(소수) : 2부터 자신의 절반이 되는 숫자까지 나누어 떨어지지 않으면 Prime
"""
count = 0
for i in range(2, 1001):

    for j in range(2, i // 2 + 1):
        if i % j == 0: #나누어 떨어진 경우
            break
        else:
            continue
    else:
        count += 1

print(count)

"""

# 2부터 1000까지 완전수(자신을 제외한 약수의 합이 자신과 같은 수)
# 6: 1+2+3=6
"""
for i in range(2, 1001):
    sum = 0
    for j in range (1, i):
        if i % j == 0:
            sum += j
        else:
            continue

    if i == sum :
        print(i)
"""

# 피보나치 수열 해보기 - 순회
"""
num1 = 1
num2 = 1
print(num1)
print(num2)

result = num1 + num2

for i in range(10):
    print(result)
    num1 = num2
    num2 = result
    result = num1 + num2

"""