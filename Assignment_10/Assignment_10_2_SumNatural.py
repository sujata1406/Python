#Sum of Natural Numbers
def SumOfNatural(No):
    Sum=0

    if No>0:
        for i in range(No+1):
            Sum=Sum+i

    return Sum


def main():

    Value=int(input("Enter number: "))

    Ret=SumOfNatural(Value)
    print("Sum of Natural numbers till the given number is:",Ret)



if __name__=="__main__":
    main()