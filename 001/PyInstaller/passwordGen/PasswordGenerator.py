#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# by pass input when developing
#nr_letters = 20
#nr_symbols = 3
#nr_numbers = 4

passlist =[]
lettersToget = nr_letters - (nr_symbols + nr_numbers)

for num in range(1,int(lettersToget)+1):
    passlist.append(random.choice(letters))
print(passlist)
for num in range(1,int(nr_symbols)+1):
    passlist.append(random.choice(symbols))
print(passlist)
for num in range(1,int(nr_numbers)+1):
    rand = random.randint(0,len(numbers)-1) #alt way instead of doing random.choice()
    passlist.append(numbers[rand])
print(passlist)
random.shuffle(passlist)
print(passlist)
password = ''.join(map(str, passlist))
print(password)

input("Press any key to exit")
