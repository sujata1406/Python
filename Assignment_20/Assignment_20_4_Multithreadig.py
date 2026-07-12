
import time
import threading

def Capital(Data):
    count=0
    for ch in Data:
        if 'A' <= ch <='Z':
            count=count+1

    print("Count of uppercase letters: ",count)
    print("TID of Capital thread is : ",threading.get_ident())
    print("TName of Capital thread is : ",threading.current_thread().name)



def Small(Data):
    count=0
    for ch in Data:
        if 'a' <= ch <='z':
            count=count+1

    print("Count of lowercase letters: ",count)
    print("TID of Small thread is : ",threading.get_ident())
    print("TName of Small thread is : ",threading.current_thread().name)



def Digits(Data):
    count=0
    for ch in Data:
        if '0' <= ch <='9':
            count=count+1

    print("Count of digits : ",count)
    print("TID of Digits thread is : ",threading.get_ident())
    print("TName of Digits thread is : ",threading.current_thread().name)



def main():
    
    Value=input("Enter string : ")

    t1 = threading.Thread(target=Small(Value), args=(100000000,))
    t2 = threading.Thread(target=Capital(Value), args=(100000000,))
    t3 = threading.Thread(target=Digits(Value), args=(100000000,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    print("Exit from main")
    

if __name__ == "__main__":
    main()