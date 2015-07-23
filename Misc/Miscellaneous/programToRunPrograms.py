__author__ = 'a-aron'
import time
import os
import sys

"""
import sys
import os
from cStringIO import StringIO
mystdout = sys.__stdout__ = StringIO()
# run Jake's program
os.system('../../ProjectEuler/euler.py') #time_game.py')fireworks
n = 3000
print >>sys.__stdout__, mystdout.getvalue()
# Tell how many questions
print >>sys.__stdin__, n
# Answer questions
while n > 0:
    #getQuestion
    #return Answer
    n -= 1
else:
    print >>sys.__stdout__, "Successful"
# os.commandline

"""
# ___________________________________________________________________________________________

if __name__ == "__main__":
    # Wipe the previous pretendFunctions.py and initiate the sequence with func0()
    with open('pretendFunctions.py', 'w') as funcs:
        string = "__author__ = 'a-aron'\n"
        string += "def func0():\n    print 0\n\n"
        # write string to pretendFunctions.py
        funcs.write(string)
    # universal path to this directory, used to find and delete .pyc's
    path = '/home/a-aron/internship/summerInt/Misc/Miscellaneous/'

    j = 0
    # For infinite loop:
    import pretendFunctions as pF
    #   j <= len(dir(pF)[dir(pF).index('func0'):len(dir(pF))])
    while j <= 5:
        """
        THIS SECTION RE-IMPORTS pretendFunctions.py
        """
        # So python doesn't know I already imported it
        del sys.modules['pretendFunctions']
        # So python doesn't just reuse the compiled version we have to delete it
        files = os.listdir(path)
        pyc_files = [f for f in files if f.endswith('.pyc')]
        # Uncomment to show all of the .pyc files that you are deleting
        # print [i for i in os.listdir(path) if i.endswith('.pyc')]
        # deletes files
        for f in pyc_files:
            os.remove(os.path.join(path, f))
        # Completes the re-import
        import pretendFunctions as pF

        # evaluates the string version so the function call can be variable
        eval("pF.func{}()".format(j))

        # append a new function to the pretendFunctions.py
        with open('pretendFunctions.py', 'a', 0) as funcs:
            funcs.write("def func{}():\n    print {}\n\n".format(j+1, j+1))

        j += 1
