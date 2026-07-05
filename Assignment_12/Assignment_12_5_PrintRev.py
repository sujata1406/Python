#print numbers till the given number starting from 1

def PrintRevNumber(No):
    Arr=[]

    for i in range(No,0,-1):
        Arr.append(i)

    return Arr

def main():
    Value=int(input("Enter number: "))

    Ret=PrintRevNumber(Value)

    print("Numbers: ",Ret )

if __name__=="__main__":
    main()