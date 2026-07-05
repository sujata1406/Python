#Display the grade as per given marks

def GradeDisplay(Mark):
    if Mark >=75:
        return "Distinction"
    
    if Mark >=60:
        return "First class"
    
    if Mark >=50:
        return "Second Class"
    
    if Mark < 50:
        return "Fail"    

def main():
    Value=int(input("Enter Marks: "))

    Ret=GradeDisplay(Value)

    print("Grade is : ",Ret )

if __name__=="__main__":
    main()