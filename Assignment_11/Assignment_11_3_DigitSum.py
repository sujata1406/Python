#Addtion of the digits in number

def SumDigit(Value):
    Sum=0

    while Value>0:
        no=Value%10
        Sum=Sum+no
        Value=Value//10
    return Sum

def main():

    Value=int(input("Enter number: "))

    Ret=SumDigit(Value)

    print("Sum of digits:",Ret)


if __name__=="__main__":
    main()