#Given number perfect or not

def PerfectNo(No):
    Sum=0
    
    for i in range(1,No):
        if No%i==0:
            Sum=Sum+i

    return Sum==No

def main():
    Value=int(input("Enter Number: "))

    Ret=PerfectNo(Value)

    if(Ret==True):
        print("Given number is Perfect Number" )

    else:
        print("Given number is not Perfect Number")


if __name__=="__main__":
    main()