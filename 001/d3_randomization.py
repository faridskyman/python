import random
import static_value
#generate random number
i=100
j=2000

a = random.randrange(i,j)
b = random.randint(100,200)
c = a * static_value.pi + b * static_value.pi
print(f"a:{a}, b:{b}, c:{c}")

#random floating point

random_float = random.random()
print(f"this gives a random float between 0-1: {random_float}")

#to get a random float form 0-10
print(f"this gives a random float between 0-10: {round(random_float*10,2)}")

#dice throw
rand_int = random.randint(1,6)
print(f"dice rolled value is: {rand_int}")

#exercise
#head and tails coin flip
flip_coin = random.randint(0,1)
coin = ""
if flip_coin==0:
 coin="head"
else:
 coin="tail"    

print(coin)