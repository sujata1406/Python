
import threading

def Thread1():
    for i in range(1,51):
        print(i,end=" ")
    print("Thread1 completed")

def Thread2():
    for i in range(50,0,-1):   
        print(i,end=" ")
    print("Thread2 completed")


def main():

    t1 = threading.Thread(target=Thread1(), args=(100000000,))
    t2 = threading.Thread(target=Thread2(), args=(100000000,))

    t1.start()
    t1.join()

    t2.start()
    
    t2.join()
    

if __name__ == "__main__":
    main()