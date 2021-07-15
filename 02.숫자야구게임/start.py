import random
import os

os.system('cls')

numbers = []

number = str(random.randint(0, 9))  # 관리 편하게 하기 위해 문자열로

for i in range(3):
    while number in numbers:  # 중복된 값 입력 안받기 위해
        number = str(random.randint(0, 9))
    numbers.append(number)

# 인덱싱을 쉽게 하기 위해 문자열로 입력받음
count_strike = 0
count_ball = 0

print(numbers)
while count_strike < 3:
    num = str(input("숫자 3자리를 입력하세요 : "))

    count_strike = 0
    count_ball = 0

    if len(num) == 3:
        for i in range(0, 3):
            for j in range(0, 3):
                if num[i] == numbers[j] and i == j:
                    count_strike += 1
                elif num[i] == numbers[j] and i != j:
                    count_ball += 1
        if count_strike == 0 and count_ball == 0:
            print("3 아웃!!")
        else:
            output = ""
            if count_strike > 0:
                output += "{} 스트라이크".format(count_strike)
            if count_ball > 0:
                output += " {} 볼".format(count_ball)
            print(output.strip())
print("게임성공")
