# Lambda function to check number is even or not 

ChkEven = lambda No : (No % 2==0)

def main():
    Value = int(input("Enter number : "))

    Ret = ChkEven(Value) 
    
    if Ret==True:
        print("It is even number")
    else:
        print("It is not even number")


if __name__ == "__main__":
    main()