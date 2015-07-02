#!/usr/bin/env python
__author__ = 'a-aron'
import time
import pickle

class FastFib2(FastFib):
    def pick_cache(self, n):
class FastFib():
    def fast_fib(self, n, m):
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

    def pickle_cache(self):
        with open(filename, 'wb') as pickled_file:
            pickle.dump(cache, pickled_file)
            pickled_file.close()

if __name__=='__main__':
    cache = {0: 0, 1:1}
    filename = "fib_cache.pickle"
    ff = FastFib()
    try:
        with open(filename, 'rb') as pickled_cache:
            cache = pickle.load(pickled_cache)
            pickled_cache.close()
    except IOError as e:
        print "No previous cache."
        # cache = {0}

    ans = int(raw_input("Number for fibos?"))

    #ff.load_pickle()
    for j in range(5, ans)[::80]:
        # tic = time.time()
        ff.fast_fib(j, j)
    tic = time.time()
    ff.fast_fib(1000, 1000)
    print time.time() - tic

    ff.pickle()
