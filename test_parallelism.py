from multiprocessing import Pool

def f(x):
  return x**2
  
arr = [1,2,3,4,5]

def main():
    p = Pool()
    res =  p.map(f, arr)
    p.close()
    p.join()
    print(res)

if __name__ == "__main__":
    main()