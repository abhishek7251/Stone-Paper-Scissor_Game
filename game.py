import random
list=['S','P','X']
chance = 0
t_chance = 3
u_score = 0
c_score = 0
prrint("ABHISHEK TANVALIYA")
print("STONE PAPER SCISSOR GAME")
print("S ->  means Stone   P ->  Paper  X ->  means Scissor ")
print("You have 3 chances ")


def for_stone():
    global u_score
    global c_score
    if u_choice == 'S' and c_choice == 'P':
        c_score = c_score + 1
        print('computer wins  the game')
    elif u_choice == 'S' and c_choice == 'X':
        print('you win the game ')
        u_score = u_score + 1
    else:
        print('Game draw')
        print("Both entered STONE")



def for_paper():
    global u_score
    global c_score
    if u_choice == 'P' and c_choice == 'S':
        print("you win the game ")
        u_score = u_score + 1
    elif u_choice == 'P' and c_choice == 'X':
        print("computer wins the game")
        c_score = c_score + 1
    else:
        print(" Game draw")
        print("both entered PAPER")

def for_scissor():
    global u_score
    global c_score
    if u_choice == 'X' and c_choice == 'S':
        print("computer wins  the game ")
        c_score = c_score + 1
    elif u_choice == 'X' and c_choice == 'P':
        print("you win th game")
        u_score = u_score + 1
    else:
        print(" Game draw")
        print("Both entered Scissor ")


while(chance<=3):

    u_choice=str(input('Enter the choice'))
    c_choice = random.choice(list)
    if u_choice == 'S':
        for_stone()
    elif u_choice == 'P':
        for_paper()
    elif u_choice == 'X':
        for_scissor()
    else:
        print("you entered wrong choice")

    chance +=1
    print(f"you have {t_chance-chance} lives left")

print("GAME OVER")

if u_score < c_score:
    print("computer wins ")
elif u_score > c_score:
    print("You wins")
else:
    print("Game Draw ")
    print("PLAY AGAIN !")


