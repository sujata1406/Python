#Count the digits in number

def CountDigit(Value):
    count=0

    while Value>0:
        no=Value%10
        count=count+1
        Value=Value//10
    return count

def main():

    Value=int(input("Enter number: "))

    Ret=CountDigit(Value)

    print("Count of digits",Ret)


if __name__=="__main__":
    main()