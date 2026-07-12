# Accept name from user and display length of its name

def CountLength(Name):
    return len(Name)

def main():
    Data=input("Enter name:")
    Ret=CountLength(Data)

    print("Length of name is :",Ret)


if __name__=="__main__":
    main()