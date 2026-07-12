#Factorial of given number

def Factorial(No):

    Mult=1
    if No>0:
        for i in range(1,No+1):
            Mult=Mult*i

    return Mult

def main():

    Value=int(input("Enter number: "))

    Ret=Factorial(Value)
    print("Factorial of the given number is:",Ret)


if __name__=="__main__":
    main()