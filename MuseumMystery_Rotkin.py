#Leah Rotkin
#Intro to Programming
#The Great Museum Escape!

'''My program is an escape room where the user has to answer three riddles correctly
and then enter the clues to win! '''

'''My mutation vs rebinding experiment'''
print("Mutation vs rebinding experiment:")
my_list = ['experiment']

'''my function where I try rebinding and mutating'''
def mutation_vs_rebinding_experiment(my_list):
    my_list.append("something")
    print(f"My list after mutating in the function {my_list}")
    my_list = ["something_else"]
    print(f"My list after rebinding in the function  {my_list}")

test_list = ['hi', 'bye']

print(f"My test list before the function call: {test_list}")
mutation_vs_rebinding_experiment(test_list)
print(f"My test list after the function call: {test_list}")

'''Mutation is visible outside the function since it changes the variable in memory
while rebinding points the variable to a completely new spot in memory leaving the
list outside untouched'''

'''My first gallery'''
def gallery_1(energy, clue_list):

    print("Welcome to Room of Numbers!")
    print("You must answer the following riddle to earn the clue of this room.")
    print("What number equals twice its own square root?")
    clue_1 = input("Your answer: ")
    if clue_1 == "4":
        print("Correct!!")
        #using boolean to test if the clue is in the list already
        if 2 not in clue_list:
            clue_list.append(2)
            print("You earned the clue: 2")
        else:
            print("You already have this clue")
    else:
        energy = reduce_energy(energy, 1)
        print("Wrong answer. Back to main menu.")
    return energy

'''My second gallery'''
def gallery_2(energy, clue_list):

    print("Welcome to Room of clocks!")
    print("You must answer the following riddle to earn the clue of this room.")
    print("Counting clockwise on a clock what is the sum of all the odd numbers?")
    clue_2 = input("Your answer: ")
    if clue_2 == "36":
        print("Correct!!")
        if 4 not in clue_list:
            clue_list.append(4)
            print("You earned the clue: 4")
        else:
            print("You already have this clue")
    else:
        energy = reduce_energy(energy, 1)
        print("Wrong answer. Back to main menu.")
    return energy

'''My third gallery'''
def gallery_3(energy, clue_list):

    print("Welcome to Room of Keys!")
    print("You must answer the following riddle to earn the clue of this room.")
    print("The door opens when key 1 and key 3 are inserted, but not when key 2 is inserted together with either key 1 or key 3.")
    print("Key 1 is inserted with key 3. Does the door open (yes/no)?")
    clue_3 = input("Your answer: ")
    if clue_3 == "yes":
        print("Correct!!")
        if 6 not in clue_list:
            clue_list.append(6)
            print("You earned the clue: 6")
        else:
            print("You already have this clue")
    else:
        energy = reduce_energy(energy, 1)
        print("Wrong answer. Back to main menu.")
    return energy

'''My function where I display the collected clues'''
def collected_clues(clue_list):
    if len(clue_list) == 0:
        print("You didn't collect any clues yet.")
    else:
        print("Your clues:")
        for clues in clue_list:
            print(f"- {clues}")

'''The function which controls reducing energy'''
def reduce_energy(energy, cost):
    energy -= cost
    #resetting energy to 0 when it goes below 0 since energy cannot be negative
    if energy <= 0:
        energy = 0
        print("Energy is less than 0, you are locked in the museum.")
    else:
        print(f"Energy is {energy} ")
    return energy

'''Function which controls escape attempts'''
def final_escape(energy, clue_list, name):
    if energy <= 1:
        print("You don't have enough energy to escape the museum.")
        return False, energy
    else:
        escape = input("Enter your clues (in the correct order, with commas): ").strip()
        if escape == "2,4,6":
            print("---Correct!!---")
            print(f"Congrats, {name}! You escaped the museum!!!")
            print(f"You collected all three clues, and escaped with {energy} Energy Points!")
            #returning True so that the main function should know
            return True, energy
        else:
            energy = reduce_energy(energy, 1)
            print("Wrong answer. Back to main menu.")
            return False, energy

'''Function that controls the menu'''
def show_menu(name, energy, clue_list):
    while True:
        print(f"Welcome, {name}! ")
        print(f"Energy: {energy}")
        print(f"Clues Collected: {len(clue_list)} of 3")

        print("1. Enter Gallery 1")
        print("2. Enter Gallery 2")
        print("3. Enter Gallery 3")
        print("4. View Collected Clues")
        print("5. Attempt to Escape")
        print("6. Quit the museum")
#trying the choice to see if it is valid
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > 6:
                raise ValueError("Invalid choice")
            return choice
        except ValueError as e:
            print(e)

'''Function that controls the entire program'''
def main():
    print("Welcome to the Museum!!")
    name = input("What is your name?")
    energy = 10
    clue = 0
    clue_list = []
    playing = True

    while playing and energy > 0:
        choice = show_menu(name, energy, clue_list)
        if choice == 1:
            energy = gallery_1(energy, clue_list)
        elif choice == 2:
            energy = gallery_2(energy, clue_list)
        elif choice == 3:
            energy = gallery_3(energy, clue_list)
        elif choice == 4:
            collected_clues(clue_list)
        elif choice == 5:
             escaped, energy = final_escape(energy, clue_list, name)
             if escaped:
                playing = False
        elif choice == 6:
            print("Quitting the museum")
            playing = False

main()

'''
Reflection:
1. I found the main function to be the hardest because I didn't realize it was needed
until the end and then I had to figure out how to redo alot of my logic.
2. I returned energy in most of my functions so that the main can access it.
3. That mutation impacts the variable even outside the function while you can only see
the effects of rebinding in the function
4. When I typed abc's instead of ints for the gallery number it gave me the error but
then stopped the program so I added a loop so that continues asking until a correct
value is entered.
'''