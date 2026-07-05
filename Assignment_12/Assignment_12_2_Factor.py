# Print factors of given number

def Table(No):
    Arr=[]

    for i in range(1,No+1):
        if No%i==0:
            Arr.append(i)

    return(Arr)

def main():
    Value=int(input("Enter number: "))

    Ret=Table(Value)

    print("Factor of given number: ",Ret )

if __name__=="__main__":
    main()