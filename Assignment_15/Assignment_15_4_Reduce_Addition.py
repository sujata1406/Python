# lambda function using reduce() which accepts list of numbers and returns addition of all numbers
from functools import reduce

Addition = lambda No1,No2 : No1+No2

def main():

    Value = int(input("Enter the number of elements:"))

    Arr=[]

    for i in range(Value):
        Arr.append(int(input()))

    addition=reduce(Addition,Arr)

    print("Addition of all numbers is : ",addition)
    
if __name__ == "__main__":
    main()