# Number is divisible by 3 and 5

def Divisible(No):

   return(No%3==0 and No%5==0)

def main():
    Value=int(input("Enter number: "))

    Ret=Divisible(Value)
    print(Ret)

    if Ret==True:
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")

if __name__=="__main__":
    main()