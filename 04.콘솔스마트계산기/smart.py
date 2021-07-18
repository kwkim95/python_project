## 윈도우 계산기의 로직을 구현해보기

# 1. 윈도우 계산기는 연산자 우선순위의 영향을 받지않고 입력받는 순서대로 계산을 한다.
# 2. 문자열 형태로 입력을 받으면 이를 각각 리스트의 원소로 넣어준다.
# 3. 연산자 +, -, *, /, =로 구분을 하여 문자열에서 숫자와 연산자를 찾아서 리스트에 넣어준다.
# 4. 숫자와 연산자로 구분하는 과정까지 진행하였으면 이제 이를 가지고 계산을 한다.
# 5. 리스트를 돌면서 연산자가 나오면 앞에 있는 순자, 연산자, 뒤에 있는 순자를 변수에 넣어주고 이들을 삭제해준다.
# 6. eval 함수를 통해 계산을 하고 결과값을 insert 함수를 통해 처음 위치에 넣어준다.
# 7. 이를 리스트의 길이가 1이 될때까지 반복한다.

import os

operator = ["+", "-", "*", "/", "="]


def string_calc(user_input, show_histroy=False):
    string_list = []
    lop = 0

    if user_input[-1] not in operator:
        user_input += "="

    for i, s in enumerate(user_input):
        if s in operator:
            if user_input[lop:i].strip() != "": # 공백 제거
                string_list.append(user_input[lop:i])
                string_list.append(s)
                lop = i + 1

    string_list = string_list[:-1]

    pos = 0
    while True:
        if len(string_list) == 1:
            break
        if len(string_list) > pos + 1 and string_list[pos] in operator:
            temp = string_list[pos - 1] + string_list[pos] + string_list[pos + 1]
            del string_list[0:3]
            string_list.insert(0, str(eval(temp)))
            pos = 0

            if show_histroy:
                print(string_list)
        pos += 1

    if len(string_list) > 0:
        result = float(string_list[0])

    return round(result, 4)


while True:
    os.system("cls")
    user_input = input("계산식을 입력하세요 : ")
    if user_input == "/exit":
        break
    result = string_calc(user_input, show_histroy=True)
    print(result)
    os.system("pause")
