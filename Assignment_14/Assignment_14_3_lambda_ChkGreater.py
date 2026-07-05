# Lambda function to check greater number

ChkGreater = lambda No1,No2 : (No1 > No2)

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = ChkGreater(Value1,Value2) 
    
    if Ret==True:
        print("Maximum number is",Value1)
    else:
        print("Maximum number is",Value2)


if __name__ == "__main__":
    main()