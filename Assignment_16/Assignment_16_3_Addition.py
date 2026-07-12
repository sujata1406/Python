#Display addtion of two numbers

def Addition(Value1,Value2):

    return Value1+Value2

def main():

    No1=int(input("Eneter first Number :"))
    No2=int(input("Eneter second Number :"))
  
    Ret=Addition(No1,No2)
 
    print("Addition is",Ret)

if __name__=="__main__":
    main()
