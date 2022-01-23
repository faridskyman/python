from queue import PriorityQueue
import random
import os
import hangmanResource
import hangmanWords
# Init variables
clear = lambda: os.system('cls')
#wordlist = ["apple","berry","cherry","bus","train","water","hospital","mouse","keyboard","telephone"]
SelectedWordList = []
maskedList = []
isSolved = False
endGame = False
userCharinput = ""
wrongLetter = 0 #if this value is >= 7 then game over, user lost
myLives = 6


# Size of the words list.
sizeofList = len(hangmanWords.wordlist)-1
# Select a word from list for the game.
selectedWordIndex = random.randint(0,sizeofList)
# An ALT way to get the randon word from list
ALTSelectedWord = random.choice(hangmanWords.wordlist)


# Update the user answer, (change _ to the char the user type if matches)
def UpdateUserAnswer(userCharInput):
    global wrongLetter
    global myLives
    matchFound = False
    #foreach char
    arrCount =0
    for letter in hangmanWords.wordlist[selectedWordIndex]:
        if letter== userCharInput:
            maskedList[arrCount] = userCharInput
            matchFound = True
        arrCount += 1
    #update wrong answered entered counter
    if(not matchFound):
        wrongLetter +=1
        myLives -= 1
        
    

#Main Program
print("Hangman game started")

#Prepare Tip
for i in hangmanWords.wordlist[selectedWordIndex]:
    SelectedWordList.append(i)
    maskedList.append("_")




#Program main loop
while(not endGame):
    clear()
    #show HangMan
    print(f"{hangmanResource.stages[myLives]}")
    # show the Tip
    print(f"{''.join(maskedList)}")
    userCharinput = input("Type a letter: ").lower()

    UpdateUserAnswer(userCharinput)    
    
    #Check if the Game is solved.    
    if ''.join(maskedList)==''.join(SelectedWordList):
        isSolved = True
        endGame = True

    if wrongLetter >= 6:
        endGame = True

    if (isSolved is True) and (endGame is True):
        clear()
        print("You have won the game!")
    elif (isSolved is False) and (endGame is True):
        clear()
        print(f"{hangmanResource.stages[myLives]}")
        print(f"You lost, the man has been hanged! the word was {''.join(SelectedWordList)}")


    
        
