# Checker whether number is positive/negative/zero

def ChkNo(Value):

    if Value==0:
        return 0
    
    elif Value>0:
        return 1
    
    else:
        return 2


def main():

    No=int(input("Enter number :"))
    Ret=ChkNo(No)

    if(Ret==0):
        print("Zero")
    
    elif(Ret==1):
        print("Positive")

    else:
        print("Negative")


if __name__=="__main__":
    main()