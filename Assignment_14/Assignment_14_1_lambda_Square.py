# Lambda function to return square of number

Square = lambda No : (No * No)

def main():
    Value = int(input("Enter number : "))

    Ret = Square(Value) 
    
    print("Square of given number is:",Ret)

if __name__ == "__main__":
    main()
