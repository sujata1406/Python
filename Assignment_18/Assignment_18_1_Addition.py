# Accept list from user and return addition of that numbers

def Addition(Data):
    Sum=0

    for i in Data:
        Sum=Sum+i

    return Sum

def main():
    Arr=[]
    
    Value=int(input("Enter number : "))

    for i in range(Value):
        num=int(input("Enter elements: "))
        Arr.append(num)

    Ret=Addition(Arr)
    print("Addition of all elements : ", Ret)


if __name__=="__main__":
    main()
