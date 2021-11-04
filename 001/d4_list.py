#list is a data str
#array
fruits = ["apple","berry","cherry"]
print(f"showing 2nd item in array: {fruits[1]}")

#update an array item
print(f"showing 2nd item in array: {fruits[0]}")
fruits[0] = "Apricot"
print(f"showing 2nd item in array: {fruits[0]}")

#add an item to the end of this list
fruits.append("durian")
fruits.extend(["eclairs","frosting","grapes","heat"])



#shows entire array on screen
print(fruits)