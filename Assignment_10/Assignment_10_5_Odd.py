## Print odd numbers till the given number

def Odd(Value):
    Arr=list()

    for i in range(1,Value+1):

        if(i%2!=0):
            Arr.append(i)

    return Arr

def main():

    Value=int(input("Enter number: "))

    Ret=Odd(Value)

    print("Odd numbers: ",Ret)


if __name__=="__main__":
    main()