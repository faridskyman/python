# using for loop with the range function.
#range (start no, end no, step value)
for number in range(1,101,10):
    print(number)

sumOfNumber=0
# add number 1 - 100
for number in range(1,101):
    sumOfNumber+=number

print(f"Total of adding number from 1 to 100 is {sumOfNumber}")



#calculate sum of all even numbers from 1 to 100, incl 1 and 100
#   2 + 4 + 6...98 + 100
sumOfEvenNumber=0

for num in range(1,101):
    if num % 2 == 0:
        sumOfEvenNumber+=num

print(sumOfEvenNumber)


#fizz buzz question
# program should print each number from 1 to 100 in turn
#   when the number if div by 3, then instead print number, it should print "fizz"
#   when the number is div by 5, then print buzz
#   when number of dif by both 3 and 5 then print fizzbuzz

printData = ""
allData = ""

for num in range(1,101):
    printData = ""
    if (num % 3 == 0) and ((num % 5 == 0)):
        printData="FizzBuzz"
    elif num % 3 == 0:
        printData="Fizz"
    elif num % 5 == 0:
        printData="Buzz"
    else:
        printData = num
    allData+=str(printData) + ", "
    #print(printData)

print(allData)
