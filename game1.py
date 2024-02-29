import random

random_number = random.randint(1, 100)

def game1(random_number):
    count=0
    while True:
        count+=1
        number = int(input('숫자를 입력해주세요'))
        if number == random_number:
            print(f"맞았습니다! {count}번째 시도 후 맞추셨습니다")
            break
        elif number < random_number:
            print("틀렸습니다 숫자를 업(up) 해보세요!")
        else:
            print("틀렸습니다 숫자를 다운(down) 해보세요!")
            
game1(random_number)