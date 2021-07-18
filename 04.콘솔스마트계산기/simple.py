import os

while True:
    os.system('cls')
    s = input("계산식 입력 : ")
    print(eval(s))  # console에서 사칙연산 가능
    if s == "0":
        break
    os.system("pause")
