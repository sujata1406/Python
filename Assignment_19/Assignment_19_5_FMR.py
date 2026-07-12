 
ChkEven=lambda No: No % 2==0            
Square=lambda No: No * No
Addition =lambda No1,No2:No1+No2

def FilterX(Task,Elements):
    Result=[]

    for no in Elements:
        Ret=Task(no)
        if(Ret==True):
            Result.append(no)

    return Result   

def MapX(Task,Elements):
    Result=[]

    for no in Elements:
        Ret=Task(no)                        
        Result.append(Ret)

    return Result


def ReduceX(Task,Elements):
    Sum=0

    for no in Elements:
        Sum=Task(Sum,no)

    return Sum

def main():
    Arr=[]
    
    Value=int(input("Enter number : "))

    for i in range(Value):
        num=int(input("Enter elements: "))
        Arr.append(num)
    print("Input data is:" ,Arr)

    fData=list(FilterX(ChkEven,Arr))
    print("Data after filter:",fData)

    mData=list(MapX(Square,fData))
    print("Data after map:",mData)

    rData=ReduceX(Addition,mData)
    print("Data after reduce:",rData)



if __name__=="__main__":
    main()