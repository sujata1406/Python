
ChkRange=lambda No:No>=70 and No<=90
Increment=lambda No: No+10
Product =lambda No1,No2:No1*No2

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
        Ret=Task(no)                        #Increment(no)
        Result.append(Ret)

    return Result


def ReduceX(Task,Elements):
    Mult=1

    for no in Elements:
        Mult=Task(Mult,no)

    return Mult

def main():
    Data=[11,23,45,15,90,80,12,9,5]

    print("Input data is:" ,Data)

    fData=list(FilterX(ChkRange,Data))
    print("Data after filter:",fData)

    mData=list(MapX(Increment,fData))
    print("Data after map:",mData)

    rData=ReduceX(Product,mData)
    print("Data after reduce:",rData)



if __name__=="__main__":
    main()