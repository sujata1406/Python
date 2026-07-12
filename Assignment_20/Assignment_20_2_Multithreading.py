
import time
import threading

def EvenFactor(No):
    Sum=0

    for i in range(1,No+1):
        if No % i==0:
            if i % 2==0:
                Sum=Sum+i
    
    print("Sum of even factors is: ",Sum)

def OddFactor(No):
    Sum=0

    for i in range(1,No+1):
        if No % i==0:
            if i % 2!=0:
                Sum=Sum+i
    
    print("Sum of Odd factors is: ",Sum)


def main():

    Value=int(input("Enter number : "))


    t1 = threading.Thread(target=EvenFactor(Value), args=(100000000,))
    t2 = threading.Thread(target=OddFactor(Value), args=(100000000,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    print("Exit from main")
    

if __name__ == "__main__":
    main()