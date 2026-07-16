class Arithmatic:


    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        self.Value1=int(input("Enter Value1 : "))
        self.Value2=int(input("Enter Value2 : "))

    def Addition(self):
        Add=self.Value1+ self.Value2
        print("Addition is : ",Add)


    def Substraction(self):
        Sub=self.Value1 - self.Value2
        print("Substraction is : ",Sub)

    def Multiplication(self):
        Mult=self.Value1 * self.Value2
        print("Multiplication is : ",Mult)

    def Division(self):
        Div=self.Value1 / self.Value2
        print("Division is : ",Div)

aobj1=Arithmatic()
aobj2=Arithmatic()
aobj3=Arithmatic()
aobj4=Arithmatic()

aobj1.Accept()
aobj1.Addition()
aobj1.Substraction()
aobj1.Multiplication()
aobj1.Division()

aobj2.Accept()
aobj2.Addition()
aobj2.Substraction()
aobj2.Multiplication()
aobj2.Division()


aobj3.Accept()
aobj3.Addition()
aobj3.Substraction()
aobj3.Multiplication()
aobj3.Division()



