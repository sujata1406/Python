# Pallindrome or not

def Pallindrome(Value):
    Rev=0
    NewValue=Value

    while Value>0:
        no=Value%10
        Rev=Rev*10+no
        Value=Value//10

    return (NewValue==Rev)


def main():

    Value=int(input("Enter number: "))

    Ret=Pallindrome(Value)

    if(Ret==True):
        print("Pallindrome")

    else:
        print("Not Pallindrome")


if __name__=="__main__":
    main()