# Reverse number

def ReverseNumber(Value):
    Rev=0

    while Value>0:
        no=Value%10
        Rev=Rev*10+no
        Value=Value//10
        print(Rev)

    return Rev

def main():

    Value=int(input("Enter number: "))

    Ret=ReverseNumber(Value)

    print("Reverse number :",Ret)


if __name__=="__main__":
    main()