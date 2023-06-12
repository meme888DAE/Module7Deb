# Page four Python 
# definition of functions 

# example function to display math 

#def displayMath():
    #print("The sum of 249*3 = 747")

#displayMath()

# Function Arguments
def displayMathAdvance(firstNumber, secondNumber ):
    answer = firstNumber + secondNumber
    print( "The sum of", firstNumber, "and", secondNumber, "is", answer )

#displayMathAdvance(7, 11)   

# Return Value Function 

def displayMathSuperAdvanced( firstNumber, secondNumber, thirdNumber):
    difference = firstNumber - secondNumber + thirdNumber
    return difference
superAdvanceDifference = displayMathSuperAdvanced(3,6,9)
print(superAdvanceDifference)

# Multiple Return Example
def applyBasicCalculations(firstNumber, secondNumber):
    
 sum = firstNumber + secondNumber
 difference = firstNumber - secondNumber
 product = firstNumber * secondNumber
 quotient = firstNumber / secondNumber

 return sum, difference, product, quotient

applyBasicCalculations(2,2)

def main():
    sum, differenceOutsideOfFunction, product, quotientReceived = applyBasicCalculations(2, 2)
    print( sum, differenceOutsideOfFunction, product, quotientReceived)

# This is a call
main; 