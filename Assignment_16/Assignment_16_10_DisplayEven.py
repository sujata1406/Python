# Display first 10 even numbers

def DisplayEven():
    Arr=[]
    Count=1
    counter=1

    while(counter<=10):
        if Count%2==0:
            Arr.append(Count)
            counter=counter+1
        Count=Count+1
    return Arr

def main():
    Ret=DisplayEven()

    print("Even numbers:",Ret)


if __name__=="__main__":
    main()