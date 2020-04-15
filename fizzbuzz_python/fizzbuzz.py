def Fizzbuzz(x):
  if x % 3 == 0:
    print ("Fizz")
  elif x % 5 == 0:
    print ("Buzz")
  elif (x % 3 == 0) & (x % 5 == 0):
    print ("Fizzbuzz")
  else :
    print (x)

for x in range(101):
  Fizzbuzz(x)

# OR 

# i = 0
# while i < 100:
#   i += 1
#   Fizzbuzz(i)