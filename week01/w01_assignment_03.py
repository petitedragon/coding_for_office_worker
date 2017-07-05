# 구현 내용

# 사용자에게 가위, 바위, 보 중 하나를 물어봅니다.
# 사용자가 가위, 바위, 보를 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가릅니다.
# 다합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝이 납니다.
# 힌트

# 리스트를 한 개를 사용하고 사용자의 입력을 받아야 합니다.
# 앞서 사용했던 임의 뽑기를 다시 사용합니다. 검색 키워드 : random, randint, shuffle
# 컴퓨터에게 가위, 바위, 보의 승패를 가르쳐줘야 합니다.

import random

rock = '바위'
scissors = '가위'
paper = '보'
rsp_list = (rock,scissors,paper)

win_cnt = 0
lose_cnt = 0


while win_cnt < 3 and lose_cnt < 3:
    # 1) 사용자 입력
    user_choice = input("{},{},{}:".format(rock,scissors,paper))
    # 2) 컴퓨터 임의 선택
    com_choice = random.choice(rsp_list)
    # 3) 3번 지거나 이기면 승패확정
    # 이기는 조건은 ...

    # user_choice & com_choice
    # rock  & paper    ==> paper
    # rock  & scissors ==> rock
    # paper & scissors ==> scissors
    
    # com_choice & user_choice
    # rock  & paper    ==> paper
    # rock  & scissors ==> rock
    # paper & scissors ==> scissors
    ##.. 이렇게는 이상함.....
    if user_choice == com_choice:
        print("비겼습니다")
    elif user_choice not in rsp_list:
        print("가위 바위 보 중 하나를 입력해주세요")
    elif ((user_choice == rock and com_choice == scissors)
          or (user_choice == scissors and com_choice == paper)
          or (user_choice == paper and com_choice == rock) ):
          win_cnt = win_cnt + 1
          print("이겼습니다")
    else:
        lose_cnt = lose_cnt + 1
        print("졌습니다")

if win_cnt == 3:
    print("사용자가 이겼습니다")
else:
    print("컴퓨터가 이겼습니다")
          
