# lambda function using filter() which accepts list of numbers and returns count of even numbers

CountEven = lambda No:No%2 ==0

def main():

    Value = int(input("Enter the number of elements:"))

    Arr=[]

    for i in range(Value):
        Arr.append(int(input()))

    countEven=list(filter(CountEven,Arr))

    print("Count of even numbers: ",len(countEven))
    
if __name__ == "__main__":
    main()