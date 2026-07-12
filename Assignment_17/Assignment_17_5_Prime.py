#Check prime number or not

def PrimeNumber(No):

    if(No<=1):
        print("Given number is not prime number")

    else:
        for i in range(2,No):
            if No % i ==0:
                print("Given number is not prime number")
                break
            
        else:
            print("Given number is prime number") 

def main():

    Value=int(input("Enter number: "))
    PrimeNumber(Value)

if __name__=="__main__":
    main()