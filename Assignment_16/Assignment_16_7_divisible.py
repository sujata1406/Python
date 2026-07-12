# return true if number is divided by 5

def ChkDivisible(No):

    return No % 5==0
      


def main():

    Value=int(input("Enter number:"))
    Ret=ChkDivisible(Value)

    print(Ret)


if __name__=="__main__":
    main()