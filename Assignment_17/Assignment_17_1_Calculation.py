#Use user defind module for calculation

import Calculation as Cal

def main():
    Value1=int(input("Enetr first number : "))
    Value2=int(input("Enetr first number : "))


    Ret=Cal.Addition(Value1,Value2)
    print("Addition is :",Ret)

    Ret=Cal.Subtraction(Value1,Value2)
    print("Subtraction is :",Ret)

    Ret=Cal.Multiplication(Value1,Value2)
    print("Multiplication is :",Ret)

    Ret=Cal.Division(Value1,Value2)
    print("Division is :",Ret)


if __name__=="__main__":
    main()
