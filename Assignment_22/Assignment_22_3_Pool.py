import multiprocessing
import os

def ChkPrime(No):

    if(No<=1):
        return False
    else:
        for i in range(2,No):
            if No % i ==0:
                return False
            
    return True  

def CountPrime(No):
    print("Process is running with PID: ",os.getpid())
    Count=0

    for i in range(1,No+1):
        if ChkPrime(i):
            Count=Count+1
    return Count


def main():

    Data=[10000,20000,30000,40000]
    Result=[]


    pobj=multiprocessing.Pool()

    Result=pobj.map(CountPrime,Data)

    pobj.close()
    pobj.join()


    print("Result is :")
    print(Result)




if __name__=="__main__":
    main()