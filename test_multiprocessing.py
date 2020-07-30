import sys
from os import getpid
from time import time
from random import randint
from math import comb
from multiprocessing import Pool, Process

# print(sys.version)

def f(x):
  print(f'Process {getpid()}')
  for _ in range(1000000):
    pass
  # return x[0] * x[1] + randint(1,100)
  return comb(x[0], x[1])

arr = [(randint(50, 100), randint(1, 50)) for _ in range(20)]

def main():
  # ----------------------
  start = time()
  res =  list(map(f, arr))
  print(f'Time: {time() - start} s')
  print(res)

  # ----------------------

  p = Pool()
  start = time()
  res =  p.map(f, arr)
  p.close()
  p.join()
  print(f'Time: {time() - start} s')
  print(res)

  # ----------------------

  start = time()
  for i in range(len(arr)):
    p = Process(target=f, args=(arr[i],))
    p.start()
    p.join()
  print(f'Time: {time() - start} s')

if __name__ == "__main__":
    main()