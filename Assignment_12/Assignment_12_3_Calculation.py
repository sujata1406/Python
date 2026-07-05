# Addition ,Subtraction,Division,Multiplication

def Addition(No1,No2):
    return No1+No2

def Subtraction(No1,No2):
    return No1-No2


def Multiplication(No1,No2):
    return No1*No2


def Division(No1,No2):
    return No1/No2


def main():
    Value1=int(input("Enter first number: "))
    Value2=int(input("Enter second number: "))

    Add=Addition(Value1,Value2)
    print("Addition of given numbers is : ",Add )

    Sub=Subtraction(Value1,Value2)
    print("Subtraction of given numbers is : ",Sub )

    Mult=Multiplication(Value1,Value2)
    print("Multiplication of given numbers is : ",Mult )

    Div=Division(Value1,Value2)
    print("Division of given numbers is : ",Div )

if __name__=="__main__":
    main()