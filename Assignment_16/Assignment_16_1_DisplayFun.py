# lambda function using map() which accepts  list of numbers and returns squares of that numbers

Square = lambda No : No ** 2


def main():

    Values = [1,2,3,4,5]

    square=list(map(Square,Values))

    print("Square of numbers are : ",square)
    
if __name__ == "__main__":
    main()
