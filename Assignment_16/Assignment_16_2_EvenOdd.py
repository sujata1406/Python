#Check whether number is evn or odd

def OddEven(Value):

    return Value % 2==0

def main():

    No=int(input("Eneter Number :"))
  
    Ret=OddEven(No)

    if Ret==True:
        print("It's Even number")
    
    else:
        print("It's Odd number")

if __name__=="__main__":
    main()
