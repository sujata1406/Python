
import threading

Sum=0
Prod=1
            
def Thread1(Data):
    global Sum
    
    print("Thread1 started")
    for i in Data:
        Sum=Sum+i

def Thread2(Data):
    print("Thread2 started")

    global Prod
    for i in Data:
        Prod=Prod*i

def main():
    Arr=[]
    
    Value=int(input("Enter number : "))

    for i in range(Value):
        num=int(input("Enter elements: "))
        Arr.append(num)
    print("Input data is:" ,Arr)

    ans=[]
    t1 = threading.Thread(target=Thread1(Arr), args=(100000000,))
    print("Sum of elements is : ",Sum)

    t2 = threading.Thread(target=Thread2(Arr), args=(10000000,))
    print("Product of elements is : ",Prod)


    t1.start()

    t2.start()

    t1.join()

    t2.join()
    

if __name__ == "__main__":
    main()