# lambda function using filter() which accepts list of strings and returns list of strings having length greater than 5 

Divisible = lambda No: No % 5 ==0 and No % 3 ==0

def main():

    Value = int(input("Enter the number of elements:"))

    Arr=[]

    for i in range(Value):
        Arr.append(int(input()))

    divisible=list(filter(Divisible,Arr))

    print("Given numbers are divisible by 3 and 5: ",divisible)
    
if __name__ == "__main__":
    main()