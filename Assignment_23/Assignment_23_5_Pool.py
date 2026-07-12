import time
import multiprocessing 
import os


def Factorial(No):
   
    fact=1
    for i in range(1,No+1):          
            fact=fact*i           
    return fact

def main():
    Data=[10,15,20,25]

    pobj=multiprocessing.Pool()
    result=pobj.map(Factorial,Data)
    print("Result is :")
    print(result)

if __name__=="__main__":
    main()