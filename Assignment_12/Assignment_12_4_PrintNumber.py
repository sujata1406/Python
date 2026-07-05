#print numbers till the given number starting from 1

def PrintNumber(No):
    Arr=[]

    for i in range(1,No+1):
        Arr.append(i)

    return Arr

def main():
    Value=int(input("Enter number: "))

    Ret=PrintNumber(Value)

    print("Numbers: ",Ret )

if __name__=="__main__":
    main()