__author__ = 'a-aron'

import sys
import os
from cStringIO import StringIO
mystdout = sys.__stdout__ = StringIO()
# run Jake's program
os.system('../../ProjectEuler/euler.py') #time_game.py')
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
