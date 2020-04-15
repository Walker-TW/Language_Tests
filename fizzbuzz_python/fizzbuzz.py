def better_fizzbuzz (x):
  for x in range(x):

    output = ""

    if ( x % 3 == 0):
      output += "Fizz"
    if ( x % 5 == 0):
      output += "Buzz"
    
    if output == "":
      print ( x )
    else:
      print ( output )

# OR

def simple_fizzbuzz(x):
  if x % 3 == 0:
    print ("Fizz")
  elif x % 5 == 0:
    print ("Buzz")
  elif (x % 3 == 0) & (x % 5 == 0):
    print ("Fizzbuzz")
  else :
    print (x)

for x in range(101):
  simple_fizzbuzz(x)

# OR 

i = 0
while i < 100:
  i += 1
  simple_fizzbuzz(i)