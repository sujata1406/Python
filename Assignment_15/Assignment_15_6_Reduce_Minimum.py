# lambda function using reduce() which accepts list of numbers and returns minimum 
from functools import reduce

Minimum = lambda No1,No2: (No1 if No1<No2 else No2)

def main():

    Value = int(input("Enter the number of elements:"))

    Arr=[]

    for i in range(Value):
        Arr.append(int(input()))

    minimum=reduce(Minimum,Arr)

    print("Minimum number is  : ",minimum)
    
if __name__ == "__main__":
    main()