
import time
import threading

def Even(No):
    Arr=[]
    Count=1
    counter=1
    while(counter<=10):
        if Count%2==0:
            Arr.append(Count)
            counter=counter+1
        Count=Count+1

    print("First 10 even numbers : ",Arr)

def Odd(No):
    Arr=[]
    Count=1
    counter=1
    while(counter<=10):
        if Count%2!=0:
            Arr.append(Count)
            counter=counter+1
        Count=Count+1
    print("First 10 odd numbers : ",Arr)


def main():

    start_time = time.perf_counter()

    t1 = threading.Thread(target=Even, args=(100000000,))
    t2 = threading.Thread(target=Odd, args=(100000000,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()
