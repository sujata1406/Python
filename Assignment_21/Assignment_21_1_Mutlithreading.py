
import threading


def ChkPrime(No):

    if(No<=1):
        return False
    else:
        for i in range(2,No):
            if No % i ==0:
                return False
       
        return True  
            
def Prime(No):
    print("Prime thread")
    for i in No:
        if ChkPrime(i):
            print(i,end=" ")
    print()

def NonPrime(No):
    print("NonPrime thread")
    for i in No:
        if not ChkPrime(i):
            print(i,end=" ")
    print()


def main():
    Arr=[]
    
    Value=int(input("Enter number : "))

    for i in range(Value):
        num=int(input("Enter elements: "))
        Arr.append(num)
    print("Input data is:" ,Arr)


    t1 = threading.Thread(target=Prime(Arr), args=(100000000,))
    t2 = threading.Thread(target=NonPrime(Arr), args=(100000000,))

    t1.start()

    t2.start()

    t1.join()

    t2.join()
    

if __name__ == "__main__":
    main()