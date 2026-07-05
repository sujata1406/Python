# Lambda function to check given number is divisible by 5 or not

Divisible = lambda No : (No % 5==0)

def main():
    Value = int(input("Enter number : "))

    Ret = Divisible(Value) 
    
    print(Ret)


if __name__ == "__main__":
    main()