name = input("Please enter your name: ")
number = int(input("Please enter a number: "))

# TODO: Make sure the number is an integer


# TODO: Print out the User's name and the number entered,
# making sure the two statements are on separate lines of output.
print("\nYour name is {}.\nThe number is {}.".format(name, number))

# TODO: Compare the number the user gave with the different
# FizzBuzz conditions. 
# *********************
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."
# *********************

is_fizz = bool(number % 3)
is_buzz = bool(number % 5)

if is_fizz is False and is_buzz is False:
    print("\n{} is a FizzBuzz number!  ^_^".format(number))
elif is_fizz is True and is_buzz is True:
    print("\n{} is neither a fizzy or a buzzy number.  =(".format(number))
elif is_fizz is False and is_buzz is True:
    print("\n{} is a Fizz number!".format(number))
elif is_fizz is True and is_buzz is False:
    print("\n{} is a Buzz number!".format(number))

# TODO: Define variables for is_fizz and is_buzz that stores 
# a Boolean value of the condition. Remember that the modulo operator, %, 
# can be used to check if there is a remainder.


# Using the variables, check the condition of the value, and print the necessary
# string




















