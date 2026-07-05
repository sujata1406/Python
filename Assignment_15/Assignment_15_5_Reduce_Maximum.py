# lambda function using reduce() which accepts list of numbers and returns maximum 
from functools import reduce

Maximum = lambda No1,No2: (No1 if No1>No2 else No2)

def main():

    Value = int(input("Enter the number of elements:"))

    Arr=[]

    for i in range(Value):
        Arr.append(int(input()))

    maximum=reduce(Maximum,Arr)

    print("Maximum number is  : ",maximum)
    
if __name__ == "__main__":
    main()