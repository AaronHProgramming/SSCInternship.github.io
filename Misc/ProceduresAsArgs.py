__author__ = 'aaron'

def integral(func, leftBound, rightBound, stepSize):
    def shift_dx(x):
        return x + stepSize
    def sum(function, leftBound, shift_dx, rightBound):
        if leftBound > rightBound:
            return 0
        else:
            return sum(function, shift_dx(leftBound), shift_dx, rightBound) + function(leftBound)
    return sum(func, leftBound + stepSize/2, shift_dx, rightBound) * stepSize
func = lambda x: x ** 2  # 3*(x**2) + 2*x + 1
print(integral(func, 1, 2, .01))

'''
def gen(x):
    y = 0
    while y >= 0:
        y += x
        print(y)
        y = yield y
g = gen(3)
g.send(None)
g.send(11)
g.send(55)
'''