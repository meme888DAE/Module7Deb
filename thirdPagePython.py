# Page three of Python 

# The While Loop example of an infinite loop - placed in comment so will not print out 

userAge = 65 

#while userAge <55:
    #print( userAge)

# second example 
while userAge <95:
    print( userAge) 
    userAge = userAge + 1


 # The For Loop example 

for currentNumber in range(5):
    print( currentNumber)

# skips value 
for currentNumber in range( 2, 11, 4):
    print( currentNumber)

# continue key word -skipping the number 5 

for currentNumber in range (1, 21 ):
    if currentNumber == 5:
        continue
    else:
        print( currentNumber) 

 # a break statement 
    for currentNumber in range ( 1, 21):
        if currentNumber == 6:
            break 
    print( currentNumber)       