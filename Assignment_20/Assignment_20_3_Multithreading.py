
import time
import threading

def EvenList(No):
    Sum=0

    for i in No:
        if i % 2==0:
            Sum=Sum+i
    
    print("Sum of even numbers from list: ",Sum)

def OddList(No):
    Sum=0

    for i in No:
        if i % 2!=0:
            Sum=Sum+i
    
    print("Sum of odd numbers from list: ",Sum)


def main():

    Arr=[]
    
    Value=int(input("Enter number : "))

    for i in range(Value):
        num=int(input("Enter elements: "))
        Arr.append(num)
    print("Input data is:" ,Arr)

    t1 = threading.Thread(target=EvenList(Arr), args=(100000000,))
    t2 = threading.Thread(target=OddList(Arr), args=(100000000,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    print("Exit from main")
    

if __name__ == "__main__":
    main()