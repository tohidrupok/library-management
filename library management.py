class User:
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password

class Book:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id
    

class laibary:
    book_id = 100
    book_list = []

    def add_book(self):
        
        name = input("Enter book name: ")
        user_id = laibary.book_id
        laibary.book_id += 1

        self.new_book = Book(name, user_id)
        self.book_list.append(vars(self.new_book))
        print('\t\tSuccessfully your book is added.')



class system(laibary) :
    user_list = []

    def create_account(self):
        name = input("Enter Your Username : ")
        password = input("Enter a password : ")
        self.new_student = User(name, password)

        self.user_list.append(vars(self.new_student)) 
        print('\t\tCongratulations.Now you are our new genaral member.')

    def get_users(self):
        return self.user_list
      

    def show_books(self):
        print('*' * 50)
        for w in self.book_list: 
            print()
            print(f"ID:{w['id']} The book name is: {w['name']}")
        print('*' * 50)


    def borrow_books(self):
        book_id = int(input("Enter the ID of the book you want to borrow: "))
        for book in self.book_list:
            if book['id'] == book_id:
                print(f"\t\tSuccessfully borrowed the book: {book['name']}")
                self.book_list.remove(book)
                return
        print("\t\tNo book found with the given ID.")

    def return_books(self):
        book_id = int(input("Enter the ID of the book you want to return: "))
        book_name = input("Enter the name of the book you want to return: ")
        returned_book = Book(book_name, book_id)
        self.book_list.append(vars(returned_book))
        print("\t\tSuccessfully returned the book.")







while True:    
    b = system()
    print("1. Create an account \n 2.Login to your account\n 3.EXIT")
    user_input = int(input("Enter Your Choice : "))

    if user_input ==3:
        break
    elif user_input ==1:
        b.create_account()

    elif user_input  == 2:
        name = input("Enter Your Username : ")
        password = input("Enter a password : ")

        flage = 0
        isAdmin = False

        if name == "admin" and password =="123":
            isAdmin = True
        #chaeck pass/id
        if isAdmin == False:                #he is not a admin
            for user in b.get_users():
                if user['username'] == name and user['password'] == password:
                    flage = 1 #find
                    break 

                
            if flage:
                while True:
                    print(f"\n {' ' * 10}\t\tWelcome to library.")
                    print("1.borrow books\n2.Available books\n3.return books\n4.Exit")
                
                    a = int(input("Enter Youe Choice : "))
                    if a ==4:
                        break
                    elif a==1:
                        b.borrow_books()
                    elif a==2:
                        b.show_books()
                    elif a == 3:
                        b.return_books()

            else:
                print("\t\tNo user found.")
                
        else:
            while True:
                print(f"\n {' ' * 10}Hello Admin sir welcome back to your laibary.")
                print("1.Add new book\n2.Available books\n3.logout")

                a = int(input("Enter Youe Choice : "))
                if a ==3:
                    break
                elif a==1:
                   b.add_book()
                elif a==2:
                    b.show_books()
                


