import time
from multiprocessing import Pool
import os


def Factorial(No):
   
    fact=1
    for i in range(1,No+1):          
            fact=fact*i           
    return fact

def main():
    Data=[10,15,20,25]

    with Pool() as p:
        result=p.map(Factorial,Data)
    print("Result is :")
    print(result)

if __name__=="__main__":
    main()