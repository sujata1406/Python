# lambda function using filter() which accepts list of numbers and returns list of odd numbers

Odd = lambda No : No % 2 !=0

def main():

    Value = int(input("Enter the number of elements:"))

    Arr=[]

    for i in range(Value):
        Arr.append(int(input()))

    odd=list(filter(Odd,Arr))

    print("Odd numbers are : ",odd)
    
if __name__ == "__main__":
    main()