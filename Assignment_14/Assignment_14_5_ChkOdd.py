# Lambda function to check number is odd or not 

ChkOdd = lambda No : (No % 2!=0)

def main():
    Value = int(input("Enter number : "))

    Ret = ChkOdd(Value) 
    
    if Ret==True:
        print("It is Odd number")
    else:
        print("It is not Odd number")


if __name__ == "__main__":
    main()