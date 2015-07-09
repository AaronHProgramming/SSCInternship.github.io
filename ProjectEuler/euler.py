__author__ = 'a-aron'

import math

def euler1(n):
    '''
    Find the sum of all the multiples of 3 or 5 below 1000.
    Function call: euler1(1000)
    Answer: 233168
    :param n: upper limit of problem
    :return: sum of numbers divisible by 3 and/or 5 below n
    '''
    sum = 0
    i = 0
    while i < n:
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        i += 1
    return sum

def euler2(n):
    '''
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    Function call: euler2(4000000)
    Answer: 4613732
    :param n: Upper limit of value in fibonacci sequence
    :return: sum of all even fibonacci numbers below n
    '''
    x, y = 1, 2
    sum = 0
    while x <= n:
        x, y = y, y + x
        if x % 2 == 0:
            sum += x
    return sum

def euler3():
    pass

if __name__ == "__main__":
    print euler1(1000)

    # TO RUN FROM COMMAND LINE:
    # python /home/a-aron/internship/summerInt/ProjectEuler/euler.py <Argument>
    #
    # Inside of python file:
    # import sys
    # print euler2(int(sys.argv[1]))
