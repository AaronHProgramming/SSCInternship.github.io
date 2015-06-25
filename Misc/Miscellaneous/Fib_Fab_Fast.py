__author__ = 'a-aron'
import time
import pickle

def fast_fib(n, m):
    if n in cache:
        return cache[n]
    elif n == m and n == max(cache.keys()) + 1:
        cache[n] = fast_fib(n-1, m) + fast_fib(n-2, m)
        return cache[n]
    elif n == max(cache.keys()) + 1:
        cache[n] = fast_fib(n-1, m) + fast_fib(n-2, m)
        return fast_fib(n+1, m)
    else:
        return fast_fib(max(cache.keys())+1, m)


cache = {0: 0, 1:1}
filename = "fib_cache.pickle"
try:
    with open(filename, 'rb') as pickled_cache:
        cache = pickle.load(pickled_cache)
        pickled_cache.close()
except IOError as e:
    print "No previous cache."
    # cache = {0}

for j in range(5, 10000)[::80]:
    # tic = time.time()
    fast_fib(j, j)
tic = time.time()
fast_fib(100000, 100000)
print time.time() - tic

with open(filename, 'wb') as pickled_file:
    pickle.dump(cache, pickled_file)
    pickled_file.close()