# Accept list from user and return Minimum number 

def Maximum(Data):
    Min=Data[0]
    for i in Data:
        if(i<Min):
            Min=i

    return Min

def main():
    Arr=[]
    
    Value=int(input("Enter number : "))

    for i in range(Value):
        num=int(input("Enter elements: "))
        Arr.append(num)

    Ret=Maximum(Arr)
    print("Minimum number is  : ", Ret)


if __name__=="__main__":
    main()