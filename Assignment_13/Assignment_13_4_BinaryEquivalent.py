 # find Binary euivalent of given number 

def BinaryEquivalent(No):
    binary=""

    while No>0:
        rem=No % 2
        binary= str(rem) + binary
        No=No // 2
    return binary




def main():

    Value=int(input("Enter number: "))

    Ret=BinaryEquivalent(Value)

    print("Binary Equivalent is : ",Ret )

if __name__=="__main__":
    main()