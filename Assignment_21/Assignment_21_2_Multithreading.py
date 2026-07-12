
import threading

            
def Thread1(Data):
    
    print("Maximum thread")
    Max=Data[0]
    for i in Data:
        if(i>Max):
            Max=i

    print("Maximum is : ",Max)
def Thread2(Data):
    Min=Data[0]
    for i in Data:
        if(i<Min):
            Min=i

    print("Minimum is : ",Min)


def main():
    Arr=[]
    
    Value=int(input("Enter number : "))

    for i in range(Value):
        num=int(input("Enter elements: "))
        Arr.append(num)
    print("Input data is:" ,Arr)


    t1 = threading.Thread(target=Thread1(Arr), args=(100000000,))
    t2 = threading.Thread(target=Thread2(Arr), args=(100000000,))

    t1.start()

    t2.start()

    t1.join()

    t2.join()
    

if __name__ == "__main__":
    main()