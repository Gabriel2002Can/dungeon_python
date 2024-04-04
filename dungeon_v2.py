#Student Name: Luis Gabriel Stedile Portella
#Program Title: 
#Description: 
import random
import csv

def main():
    monsters_list = []
    user_continue = ""
    with open("monsters.csv","r") as reader:
        monster_reader = csv.reader(reader)
        for monster in monster_reader:
            monsters_list.append(monster)

    while user_continue != "q":
        user_continue = str.lower(input("Hit any key to continue ('Q' or 'q' to quit): "))
        if user_continue == "q":
            break
        total_hp = 0
        print()

        while total_hp < 1 or total_hp > 200:
            try:
                total_hp = int(input("Please enter your initial hit points (1-200): "))
                if total_hp < 1 or total_hp > 200:
                    print("You do not listen very well do you? Think you are going to survive this dungeon?")
            except:
                print("You do not listen very well do you? Think you are going to survive this dungeon?")

        current_hp = total_hp
        print("-"*50)
        print("-"*50)

        while current_hp > 0: #being attacked
            random_monster = random.randint(1,len(monsters_list)-1)
            current_hp -= int(monsters_list[random_monster][2])

            if current_hp < 0 or current_hp == 0:
                current_hp = 0
            print(f"You were attacked by a {monsters_list[random_monster][0]} with a {monsters_list[random_monster][1]} attack for {monsters_list[random_monster][2]} damage. Current hit points: {current_hp}")
            
        print(f"That was sad. And brief. At least the {monsters_list[random_monster][0]} feels better about himself!!!\n")

    print("That's it. Retreat in fear and warn your friends!")

if __name__ == "__main__":
    main()