from MarvellousNum import ChkPrime

def ListPrime():
    Arr=[]
    Sum=0
    Value=int(input("Enter number : "))

    for i in range(Value):
        num=int(input("Enter element: "))
        Arr.append(num)


    for i in Arr:
        if ChkPrime(i):
            Sum=Sum+i

    print("Addition of prime numbers: ",Sum)
   

def main():
        ListPrime()
        

if __name__=="__main__":
    main()