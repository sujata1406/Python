class Numbers:

    def __init__(self):
        self.Value=int(input("Enter Value : "))

    def ChkPrime(self):
        if(self.Value<=1):
            print("Given number is not prime number")

        else:
            for i in range(2,self.Value):
                if self.Value % i ==0:
                    print("Given number is not prime number")
                    break
            
            else:
                print("Given number is prime number") 

    def ChkPerfect(self):
        Sum=0
    
        for i in range(1,self.Value):
          if self.Value%i==0:
            Sum=Sum+i

        if Sum==self.Value:
            print("Perfect Number")

        else:
            print("Not perfect number")


    def Factors(self):
        Arr=[]
        for i in range(1,self.Value+1):
            if self.Value % i==0:
                Arr.append(i)
        print("Factors are : ", Arr)


    def SumFactors(self):
        Sum=0
        for i in range(1,self.Value+1):
            if self.Value % i==0:
                Sum=Sum+i
        print("Sum of Factors : ", Sum)


Nobj1=Numbers()

Nobj1.ChkPrime()
Nobj1.ChkPerfect()
Nobj1.Factors()
Nobj1.SumFactors()

Nobj2=Numbers()


Nobj2.ChkPrime()
Nobj2.ChkPerfect()
Nobj2.Factors()
Nobj2.SumFactors()