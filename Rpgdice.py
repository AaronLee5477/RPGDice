import random

## simulates a d20 attack roll
def attack_roll(number):
    base = random.randint(1, 20)
    result = base + int(number)
    if base == 1:
        print("Oh no!! You critically missed!!")
    elif base == 20:
        print("Awesome!! A critical hit!!")
    else:
        print(str(base) + " + " + str(int(number)))
        print("You hit an Armor Class of " + str(result))


while True:
    attack_modifer = input("What is your Attack Modifier? ")
    attack_roll(attack_modifer)
    attack = input("Can you attack again? (Y or N): ")
    if attack.upper() == 'N':
        break
    
print("Your attack is done!!")
