import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

artComputer = '''
                                _            
                                | |           
  ___ ___  _ __ ___  _ __  _   _| |_ ___ _ __ 
 / __/ _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__|
| (_| (_) | | | | | | |_) | |_| | ||  __/ |   
 \___\___/|_| |_| |_| .__/ \__,_|\__\___|_|   
                    | |                       
                    |_|                      
'''

artFlower = '''
                __ .-~-.   .~``~,._
              .~  `     \ /     .  `\\
              |     \    |   .'     |
        _      \     `.  |  /    __/
     .~` `'. .--;.       ,.O  -~`   `\\
     \  '-. |     `-  o.O/o, __       |
      '-.,__ \    .-~' `\|o `  ~.    /_
        _.--'/   `    ,  /  \        | `~-.,
       /     |       /  :    '._    / -.    `\\
 jgs  /   .-' '.___.;   `      \`--'\    `    |
     |          /    \         /     '.__,.--,/
     '--..,___.'      `~--'--~'
     '''

artTie = '''
 _   _      
| | (_)     
| |_ _  ___ 
| __| |/ _ \\
| |_| |  __/
 \__|_|\___|
 '''


choices = [rock,paper,scissors]
u = int(input("Your choice: 0 for Rock, 1 for Paper and 2 for Sissors: ")) #user choice
c = random.randint(0,2) #computer choice

print(f"You:{choices[u]} \n Computer:{choices[c]}")


# Rules:
#   Rock(0) wins against scissors(2).
#   Scissors(2) win against paper(1).
#   Paper(1) wins against rock(0).

if (u==0 and c==2):
 win=1
elif (u==2 and c==1):
 win=1
if (u==1 and c==0):
 win=1
elif (u==0 and c==1):
 win=2
elif (u==1 and c==2):
 win=2     
if (u==2 and c==0):
 win=2
elif (u==c):
 win=-1     


if (win==1):
 print("YOU Win!")
 print(artFlower)
elif (win==2):
 print("Computer wins.")
 print(artComputer)
else:
 print("No one wins.")
 print(artTie)
 