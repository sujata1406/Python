# lambda function using filter() which accepts list of strings and returns list of strings having length greater than 5 

LenStr = lambda Str: (len(Str)>5,Str)

def main():

    Value = int(input("Enter the number of elements:"))

    Arr=[]

    for i in range(Value):
        Arr.append(input())

    lenStr=list(filter(LenStr,Arr))

    print("Strings having length greater than 5: ",lenStr)
    
if __name__ == "__main__":
    main()