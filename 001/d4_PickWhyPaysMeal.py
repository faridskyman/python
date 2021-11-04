import random
# Split string method
#names_string = input("Give me everybody's names, separated by a comma. ")
names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

arrCount = len(names)
randomKey = random.randint(0,arrCount-1)
print(f"person to pay: {names[randomKey]}")
