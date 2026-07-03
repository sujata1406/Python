#Check greater between two numbers

def ChkGreater(No1,No2):
    return No1>No2 

def main():

    Value1=int(input("Enter first number: "))
    Value2=int(input("Enter second number:"))

    Ret=ChkGreater(Value1,Value2)

    if(Ret==True):
        print(Value1,"is Greater")

    else:
        print(Value2,"is Greater")    

if __name__=="__main__":
    main()
