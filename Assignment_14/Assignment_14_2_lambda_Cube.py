# Lambda function to return cube of number

Cube = lambda No : (No * No * No)

def main():
    Value = int(input("Enter number : "))

    Ret = Cube(Value) 
    
    print("Cube of given number is:",Ret)

if __name__ == "__main__":
    main()