#Display numbers in reverse order

def ReverseNo(Value):

    for i in range(Value,0,-1):
        print(i)

def main():

    No=int(input("Enter number :"))
    ReverseNo(No)

if __name__=="__main__":
    main()