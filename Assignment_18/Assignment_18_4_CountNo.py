# Accept list from user and return count of particular number

def Maximum(Data,No):
    Count=0
    for i in Data:
        if i==No:
            Count+=1
    return Count

def main():
    Arr=[]
    
    Value=int(input("Enter number : "))


    for i in range(Value):
        num=int(input("Enter elements: "))
        Arr.append(num)
    
    Element=int(input("Enter element to search in list : "))

    Ret=Maximum(Arr,Element)
    print("Count of number is  : ", Ret)


if __name__=="__main__":
    main()