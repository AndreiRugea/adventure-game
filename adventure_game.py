import time
import random

items = []

monsters = ["dragon", "werewolf", "goblin", "leprechaun",
            "troll", "erlking", "Yeti"]


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt)
        if option1 == response:
            break
        elif option2 == response:
            break
    return response


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open "
                "field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + monster + " is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def main(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    response = valid_input("What would you like to do?\n"
                           "(Please enter 1 or 2.)\n", "1", "2")
    if response == "1":
        house(items)
        response = valid_input("Would you like to (1) fight or (2) "
                               "run away?\n", "1", "2")
        if response == "1":
            fight(items)
        elif response == "2":
            field()
    elif response == "2":
        cave(items)


def fight(items):
    if "Sword of Ogoroth" not in items:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the " + monster + ".")
        print_pause("You have been defeated!")
        response = valid_input("Would you like to play again? "
                               "(y/n)\n", "y", "n")
        if response == "y":
            print_pause("Excellent! Restarting the game ...")
            play_game()
        elif response == "n":
            print_pause("Thanks for playing! See you next time.")
    elif "Sword of Ogoroth" in items:
        print_pause("As the " + monster + " moves to attack, you "
                    "unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
        print_pause("But the " + monster + " takes one look at "
                    "your shiny new toy and runs away!")
        print_pause("You have rid the town of the " + monster + "."
                    "You are victorious!")
        response = valid_input("Would you like to play again? "
                               "(y/n)\n", "y", "n")
        if response == "y":
            print_pause("Excellent! Restarting the game ...")
            play_game()
        elif response == "n":
            print_pause("Thanks for playing! See you next time.")


def cave(items):
    print_pause("You peer cautiously into the cave.")
    if "Sword of Ogoroth" in items:
        print_pause("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        main(items)
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the "
                    "sword with you.")
        print_pause("You walk back out to the field.\n")
        items.append("Sword of Ogoroth")
        main(items)


def field():
    print_pause("You run back into the field. Luckily, you "
                "don't seem to have been followed.\n")
    main(items)


def house(items):
    if "Sword of Ogoroth" not in items:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens "
                    "and out steps a " + monster + ".")
        print_pause("Eep! This is the " + monster + "'s house!")
        print_pause("The " + monster + " attacks you!")
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    elif "Sword of Ogoroth" in items:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens "
                    "and out steps a " + monster + ".")
        print_pause("Eep! This is the " + monster + "'s house!")
        print_pause("The " + monster + " attacks you!")


def play_game():
    items = []
    global monster
    monster = random.choice(monsters)
    intro()
    main(items)


play_game()
if __name__ == "__main__":
    main(items)
