#Intermediate
def get_number(lower, upper):

    try:
        numChoice = int(input('Enter a number between ' + str(lower) + ' and ' + str(upper) + ': '))

        if int(lower) < numChoice < int(upper):
            print("The character for " + str(numChoice) + " is ", chr(numChoice))
        else:
            print("Number must be between " + str(lower) + " and " + str(upper))
            get_number(lower, upper)
    except ValueError:
        print("That's not a number!")
        get_number(lower, upper)

#numChoice = int(input("Enter a number between 33 and 127: "))
#print("The character for " + str(numChoice) + " is ", chr(numChoice))

#try:
    #numChoice = int(input("Enter a number between 33 and 127: "))

    #if 33 < numChoice < 127:
        #print("The character for " + str(numChoice) + " is ", chr(numChoice))
   # else:
        #print("Number must be between 33 and 27")
#except ValueError:
    #print("That's not a number!")

charChoice = input("Enter a character: ")
print("The ASCII code for " + charChoice + " is ", ord(charChoice))

get_number(33, 127)
i = 33

while 33 <= i < 127:
    chari = chr(i)
    print('{:3} {:>4}'.format(i, chari))

    i += 1