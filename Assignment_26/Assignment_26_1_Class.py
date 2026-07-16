class Demo:
    Value=2
    def __init__(self,A,B):
        self.No1=A
        self.No2=B

    def fun(self):
        print("In instance function fun")
        print(self.No1)
        print(self.No2)


    def gun(self):
        print("In instance function gun")
        print(self.No1)
        print(self.No2)

dobj1=Demo(11,12)
dobj2=Demo(51,10)

dobj1.fun()
dobj1.gun()

dobj2.fun()
dobj2.gun()

