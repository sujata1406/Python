# Print table of given number

def Table(No):
    Arr=[]

    for i in range(1,11):
        Mult=No*i

        Arr.append(Mult)

    return(Arr)

def main():
    Value=int(input("Enter number: "))

    Ret=Table(Value)

    print("Table of",Value ,"is:",Ret )

if __name__=="__main__":
    main()
