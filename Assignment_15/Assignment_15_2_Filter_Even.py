# lambda function using filter() which accepts list of numbers and returns list of even numbers

Even = lambda No : No % 2 ==0

def main():

    Value = int(input("Enter the number of elements:"))
    Arr=[]

    for i in range(Value):
        Arr.append(int(input()))
    even=list(filter(Even,Arr))

    print("Even numbers are : ",even)
    
if __name__ == "__main__":
    main()