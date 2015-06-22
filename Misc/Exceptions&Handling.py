__author__ = 'aaron'

try:
    n = int(input("Please enter a float."))
except ValueError:
    print("Haha I lied.  You have to type in a string.")
len = len(input("Type in an int."))
print("The length of your string is {}".format(len))
try:
    raise IOError()
    raise ValueError()
except ValueError:
    print("you win the game")
except IOError:
    print("you lose the game")
