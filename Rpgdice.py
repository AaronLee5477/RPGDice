import random

def attack_roll(number): ## simulates a d20 attack roll
    base = random.randint(1, 20)
    result = base + int(number)
    if base == 1:
        print("Oh no!! You critically missed!!")
    elif base == 20:
        print("Awesome!! A critical hit!!")
    else:
        print(str(base) + " + " + str(int(number)))
        print("You hit an Armor Class of " + str(result))

def damage_roll():  ## simulates damage roll based on user input
    total_damage = 0
    i = 0
    dice_size = int(input("What number-sided dice does your attack use? "))
    number_of_dice = int(input("How many damage dice does your attack use? "))
    damage_modifier = int(input("Do you have a damage modifier (Enter 0 if no modifier)? "))

    while i < number_of_dice:
        single_dice = random.randint(1, dice_size)
        total_damage += single_dice
        i += 1

    total_damage += damage_modifier

    print("You did " + str(total_damage) + " points of damage!!")




## Begin program
while True:

    while True:
        attack_modifer = input("What is your Attack Modifier? ")

        try:  ## Ensures valid integer input
            val = int(attack_modifer)
            break
        except ValueError:
            print("That is not a valid modifier")

    attack_roll(attack_modifer)

##### hit/miss prompt &
    while True:
        hit_prompt = input("Did you hit? (Y or N): ")
        if hit_prompt.upper() == 'N' or hit_prompt.upper() == "Y":
            break
        else:
            print("Invalid response.")
    if hit_prompt.upper() == "Y":
        damage_roll()


    while True:  ###  This section allows you to attack again and check for valid responses
        attack = input("Can you attack again? (Y or N): ")
        if attack.upper() == 'N' or attack.upper() == "Y":
            break
        else:
            print("Invalid response.")
    if attack.upper() == "N":
        break
    else:
        continue

print("Your attack is done!!")
