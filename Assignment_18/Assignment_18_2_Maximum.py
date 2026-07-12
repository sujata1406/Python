# Accept list from user and return Maximum number 

def Maximum(Data):
    Max=Data[0]
    for i in Data:
        if(i>Max):
            Max=i

    return Max

def main():
    Arr=[]
    
    Value=int(input("Enter number : "))

    for i in range(Value):
        num=int(input("Enter elements: "))
        Arr.append(num)

    Ret=Maximum(Arr)
    print("Maximum number is  : ", Ret)


if __name__=="__main__":
    main()