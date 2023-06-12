# Page Two of Python 


# These are examples of Boolean Expressions 
# If then statements & Decision Structures
# This is regarding the month that a kindergardener must be 5 years old in order to enroll in Kindergarden 

userMonth = 9

if userMonth < 9: 
    print( " You can not enter Kindergarden until next year ")

# If Else Example 

userMonth = 9

if userMonth < 9 : 
    print( " You can not enter Kindergarden until next year ")
else:
    print( " Congratulations: can enroll in Kindergarden ")

# These are examples of relational operators using elif

if userMonth > 6: 
    print( " Sorry, you will have to attend Kindergarden next year")
elif userMonth < 10:
    print( " Congratulations: You can enroll for Kindergarden this year")
elif userMonth > 8 :
    print( "You are really close, but will still have to wait until next year to enroll in Kindergarden" )
elif userMonth > 12: 
    print( "You sure that you aren't already in Kindergarden? " )


# This is an example of using equal sign 
userAge= 13

if userAge == 13:
    print( "we have a match ")
else: 
    print( "Your age isn't 13 so you will not bw able to go to highschool")

# Logical Operators 
# use of AND  logical operator in Boolean expression 
# this is regarding Presidental Election must be 18 by Nov in order to Vote

REQUIRED_Age = 18
REQUIRED_Month = 11

userAge = 18
userMonth = 11

if userAge >= REQUIRED_Age and userMonth >= REQUIRED_Month:
    print( " You are able to vote ")
else:
    print( " Sorry, you can not vote, you have not met the age limit for voting in this election.")


# use of the OR  logical operator 

REQUIRED_MONEY = 6.50
REQUIRED_AGE = 12

userAge = 13 
userMoney = 20  

if userAge < REQUIRED_AGE or userMoney <REQUIRED_MONEY:
    print( "You have to meet the requirements ")
else:
    print( "Enjoy the movie" )