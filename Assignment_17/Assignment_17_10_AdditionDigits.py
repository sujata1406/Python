#Count the digits in number

def CountDigit(Value):
    Sum=0

    while Value>0:
        no=Value%10
        Sum=Sum+no
        Value=Value//10

    return Sum

def main():

    Value=int(input("Enter number: "))

    Ret=CountDigit(Value)

    print("Addition of digits",Ret)


if __name__=="__main__":
    main()