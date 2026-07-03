# Check Vowel or not

def Vowel(Data):

   return (Data=='a' or Data=='e' or Data=='i' or Data=='o' or Data=='u' or
           Data=='A' or Data=='E' or Data=='I' or Data=='O' or Data=='U')

def main():

    Value=input("Enter character: ")

    Ret=Vowel(Value)

    if(Ret==True):
        print("The given character is Vowel")

    else:
        print("The given characcter is Not Vowel")


if __name__=="__main__":
    main()
