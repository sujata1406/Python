class BookStore:

    NoOfBooks=0

    def __init__(self,A,B):
        self.Name=A
        self.Author=B
        BookStore.NoOfBooks=BookStore.NoOfBooks+1

    def Display(self):
        print(self.Name,"by ",self.Author, "No. of books ",BookStore.NoOfBooks)


bobj1=BookStore("Linux System Programming","Robert Love")
bobj1.Display()

bobj2=BookStore("C Programming ","Dennis Ritchie")
bobj2.Display()

