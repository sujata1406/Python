import time
from multiprocessing import Pool
import os


def SumSquare(No):
    print("Process is running with PID: ",os.getpid())
    Sum=0

    for i in range(1,No+1):          
            i=i*i           
            Sum=Sum+i
    return Sum


def main():

    Data=[1000000,2000000,3000000,4000000]

    with Pool() as p:
        result=p.map(SumSquare,Data)


    print("Result is :")
    print(result)

if __name__=="__main__":
    main()
