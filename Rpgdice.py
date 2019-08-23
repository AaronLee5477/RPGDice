import random


while True:

### Prompts user for attack modifier then simulates d20 roll
    while True:
        try:
            attack_modifer = int(input("What is your Attack Modifier? "))
            break
        except ValueError:
            print("That is not a valid modifier")

    base = random.randint(1, 20)
    result = base + int(attack_modifer)

### Automatically assumes a miss and continues the program
    if base == 1:
        print("Oh no!! You critically missed!!")

#### Automatically assumes a hit and calcutes double damage
    elif base == 20:
        print("Awesome!! A critical hit!!")
        total_damage = 0
        i = 0
        while True:
            try:
                dice_size = int(input("What number-sided dice does your attack use? "))
                break
            except ValueError:
                print("That is not a valid modifier")

        while True:
            try:
                number_of_dice = int(input("How many damage dice does your attack use? "))
                break
            except ValueError:
                print("That is not a valid modifier")

        while True:
            try:
                damage_modifier = int(input("Do you have a damage modifier (Enter 0 if no modifier)? "))
                break
            except ValueError:
                print("That is not a valid modifier")

        crit_dice = number_of_dice * 2
        while i < crit_dice:
            single_dice = random.randint(1, dice_size)
            total_damage += single_dice
            i += 1

        total_damage += damage_modifier

        print("You did " + str(total_damage) + " points of damage!!")

### Checks to see if user hits then proceeds to damage roll simulation
    else:
        print(str(base) + " + " + str(int(attack_modifer)))
        print("You hit an Armor Class of " + str(result))
        while True:
            hit_prompt = input("Did you hit? (Y or N): ")
            if hit_prompt.upper() == 'N' or hit_prompt.upper() == "Y":
                break
            else:
                print("Invalid response.")
        if hit_prompt.upper() == "Y":
            total_damage = 0
            i = 0

            while True:
                try:
                    dice_size = int(input("What number-sided dice does your attack use? "))
                    break
                except ValueError:
                    print("That is not a valid modifier")

            while True:
                try:
                    number_of_dice = int(input("How many damage dice does your attack use? "))
                    break
                except ValueError:
                    print("That is not a valid modifier")

            while True:
                try:
                    damage_modifier = int(input("Do you have a damage modifier (Enter 0 if no modifier)? "))
                    break
                except ValueError:
                    print("That is not a valid modifier")

            while i < number_of_dice:
                single_dice = random.randint(1, dice_size)
                total_damage += single_dice
                i += 1

            total_damage += damage_modifier

            print("You did " + str(total_damage) + " points of damage!!")

###  This section allows you to attack again and check for valid responses
    while True:
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
