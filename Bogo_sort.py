from random import *
from time import *

seed()
x = []
for i in range(0, 100):
    x.append(randint(0, 100))

def inorder(x):
    i = 0
    j = len(x)
    while i + 1 < j:
        if x[i] > x[i + 1]:
            return False
        i += 1
    return True

def bogo(x):
    while not inorder(x):
        shuffle(x)
    return x

start = time()
print ("Before: ", x)
x = bogo(x)
print ("After: ", x)
print ("%.2f seconds" % (time() - start))
