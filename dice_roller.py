import random


def roll_dice():
    die_one = random.choice(range(1,7))
    
    if die_one == 1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
    if die_one == 2:
            print("[-----]")
            print("[ 0   ]")
            print("[     ]")
            print("[   0 ]")
            print("[-----]")
    if die_one == 3:
            print("[-----]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[-----]")
    if die_one == 4:
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
    if die_one == 5:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
    if die_one == 6:
            print("[-----]")
            print("[0 0 0]")
            print("[     ]")
            print("[0 0 0]")
            print("[-----]")   

    return [ die_one ]

def start():
    try:
        user_ask = input('Do you want to roll dice ( Yes or No ) : ')
    except ValueError:
        print('Invalid input response')
        return
    if user_ask.lower() == 'yes':
        dice_output = roll_dice()
        print(dice_output)
        start()
    if user_ask.lower() == 'no':
        return
    print('Thanks for checking ')
    return

if __name__ == "__main__" :
    start()


 
