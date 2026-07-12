import multiprocessing
import os
import time

 

def Sum(No):
    print("Process is running with PID: ",os.getpid())
    Sum=0
    for i in range(1,No+1):
        i=i**5
        Sum=Sum+i
      
    return Sum


def main():

    Data=[1000000,2000000,3000000,4000000]
    Result=[]

    start_time=time.perf_counter()

    pobj=multiprocessing.Pool()

    Result=pobj.map(Sum,Data)

    pobj.close()
    pobj.join()
    end_time=time.perf_counter()


    print("Result is :")
    print(Result)

    print(f"Time required:{end_time-start_time:.4f} seconds")





if __name__=="__main__":
    main()