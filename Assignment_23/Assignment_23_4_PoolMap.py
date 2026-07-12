import time
from multiprocessing import Pool
import os


def OddCount(No):
    print("Process is running with PID: ",os.getpid())
    Count=0

    for i in range(1,No+1):
        if i % 2!=0:
            Count=Count+1
    return Count


def main():

    Data=[1000000,2000000,3000000,4000000]

    with Pool() as p:
        result=p.map(OddCount,Data)


    print("Result is :")
    print(result)

if __name__=="__main__":
    main()