# Accept number from user and print that number of *

def DisplayStar(No):

        print("*"*No)

def main():

    Value=int(input("Enter number:"))
    DisplayStar(Value)


if __name__=="__main__":
    main()