import random

a = input('Start?\n Yes/No\n')
b = None

while a == 'Yes':
    user_action = input("\nChoose:rock, paper, ciccor\n")
    possible_act = ['rock', 'paper', 'ciccor']  # r,p,c
    comp_act = random.choice(possible_act)
    print(f"\n Your choice: {user_action} Computer choise: {comp_act}.\n")

    if user_action == comp_act:
        print('Draw')
    elif user_action == 'rock':
        if comp_act == 1:
            print('comp wins')
        else:
            print('you win')
    elif user_action == 'paper':
        if comp_act == 2:
            print('you win')
        else:
            print('comp wins')
    elif user_action == 'ciccor':
        if comp_act == 0:
            print('comp wins')
        else:
            print('you win')
    a = input('Play again?\nYes/No\n ')
