import random
import os
number = random.randint(1, 99)

cnt = 0
os.system('cls')

while True:
    cnt += 1
    user_input = int(input("숫자 몇을 입력받을까요? {}번째 시도입니다.".format(cnt)))

    if number == user_input:
        print("정답입니다. 답은 {}이었습니다".format(number))
        break
    else:
        if(number > user_input):
            print("정답보다 작은 값을 입력하였습니다.")
        elif(number < user_input):
            print("정답보다 큰 값을 입력하였습니다.")
