import time
import multiprocessing
import os


def SumOdd(No):
    print("Process is running with PID: ",os.getpid())
    Sum=0

    for i in range(1,No+1):
        if i % 2!=0:
            Sum=Sum+i
    return Sum


def main():

    Data=[10000000,20000000,30000000,40000000]
    Result=[]


    pobj=multiprocessing.Pool()

    Result=pobj.map(SumOdd,Data)

    pobj.close()
    pobj.join()


    print("Result is :")
    print(Result)




if __name__=="__main__":
    main()