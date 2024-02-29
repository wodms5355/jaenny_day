import random

choice= random.choice(["가위","바위","보"])
choice=['가위','바위','보']

def  game2(choice):
    count=0
    count2=0
    count3=0
    count4=0
    while choice:
        count+=1
        you=input('가위,바위,보 중 하나를 선택하세요')
        if you == choice:
                count2+=1
                print("무승부 입니다 다시 도전하시겠습니까?")
        elif you == "가위" and \
            choice == "주먹" or\
            you == "보" and \
            choice == "가위" or\
            you == "주먹" and \
                choice == "보":
            count3+=1
            print("땡! 졌습니다. 다시 도전하시겠습니까?")
        else:
            count4+=1
            print(f"우와 정답입니다! 지금까지 총 {count}번 진행하셨습니다.")
        you=input('게임을 계속 하시겠습니까?')
        if you == "y" or\
            you == "Y" :
            print(game2)
        elif you == "n" or\
            you == "N" :
            print(f"지금까지 무승부는{count2}번, 승리는{count4}번, 패배는{count3}번 하셨습니다")
            break
game2(choice)