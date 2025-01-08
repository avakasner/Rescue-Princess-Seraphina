# group project with Ava Kasner and Jake Potter (first of many)

import time

def displayIntro():
    print('''The kingdom of Eldoria is in despair—Princess Seraphina has been captured by the dark sorcerer Malgrin and locked away in the Obsidian Spire.''')
    time.sleep(2)
    print()

def choosePath():
    path = ''
    while path != 'woods' and path != 'prairie':
        print("Quest: Rescue Princess Seraphina")
        print('In front of you are two paths. One leads you to the dark woods and the other to a beautiful prairie. Which path will you take? (woods or prairie)')
        path = input().lower()
        if path != 'woods' and path != 'prairie':
            print("Error: Invalid choice. please type in either 'woods' or 'prairie'.\n")

    return path

def checkPath(chosenPath):
    if chosenPath == 'woods':
        print()
        time.sleep(2)
        print('You have chosen wisely, and as your journey was much scarier than anticipated, you came out in one piece. Now you are ready to go to the tower.')
        print()
        fightDragon()  # Proceed to the dragon fight
        chosenWeapon = chooseWeapon()
        checkWeapon(chosenWeapon)
    if chosenPath == 'prairie':
        print('You walked into the prairie but bumped into a gnome. Now a herd of them are coming after you. You must run back.')
        time.sleep(2)
        print()
        path = choosePath()  # Choose path again
        checkPath(path)  # Retry path


def fightDragon():
    time.sleep(2)
    print('You see Princess Seraphina up in the tower! You walk towards the entrance but...')
    time.sleep(2)
    print('BAMMMM')
    time.sleep(2)
    print('The fortress is guarded by a fearsome dragon with scales like iron and breath of fire. You must defeat the dragon in a brawl to get to the princess.')

def chooseWeapon():
    weapon = ''
    print()
    time.sleep(2)
    print('Next to you is a chest.')
    time.sleep(3)
    while weapon != 'sword' and weapon != 'bow':
        print('You open it. You see a sword and a bow and arrow. Which will you choose to fight the dragon? (sword or bow)')
        weapon = input().lower()

    return weapon

def checkWeapon(chosenWeapon):
    if chosenWeapon == 'bow':
        print("It seems you have luck on your side.\nYou managed to shoot your last arrow clean through the dragon's throat, and the master key to the tower falls out of his throat along with a pool of blood.")
        time.sleep(2)
        print("You have made it up the stairs and unlocked the princess from her chambers. She greets you with joy and gratitude. \nShe immediately falls in love and asks you to marry her. You live happily ever after as the prince and princess of Eldoria!")
        time.sleep(2)
        print('THE END')
    else:
        print('The sword broke upon impact with the dragon’s iron-like scales, and you have been swallowed whole.')
        time.sleep(2)
        print('THE END')
        playAgain()

def playAgain():
    time.sleep(2)
    print('Do you want to play again? (yes or no)')
    again = input().lower()
    if again == 'yes' or again == 'y':
        startGame()
    else:
        print('Thanks for playing!')

def startGame():
    displayIntro()
    path = choosePath()
    checkPath(path)

# Start the game
startGame()

