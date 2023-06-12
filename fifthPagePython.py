# Page Five Python 
# examples of files and exceptions

# writing a file 
#def main ():
    #testFile = open ("testfile.txt", "w" )

    #testFile.write("5") 
    #testFile.write (("10") + "\n")
    #testFile.write (str (15))
#main()    

# reading from a file 
#def main ():

    #testFile = open ("testfile.txt", "r" )

    #line = testFile.readline()

    #while line != "":
       # print(line)
        #line = testFile.readline()

        #testFile.close()

#main() 

# specific exceptions  
def main ():
    try:
        testFile = open ("testfile.txt", "r" )

        line = testFile.readline()

        while line != "":
            print(line)
            line = testFile.readline()
    except ValueError:
        print ("uh, something is wrong")
    except FileNotFoundError:
        print("Hello, Your file doesnot exist. Please fix it")    
    else:
        print("All systems are functioning")
    finally:
        testFile.close()

main()

# all exceptions 
def main ():
    try:
        testFile = open ("testfile.txt", "r" )

        line = testFile.readline()

        while line != "":
            print(line)
            line = testFile.readline()
    except Exception as potentialError:
        print( potentialError)
    else:
        print("All systems are functioning")
    finally:
        testFile.close()
        print("End of program")

main()