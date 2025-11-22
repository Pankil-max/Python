class LibraryManagement:
    def __init__(self):
        self.noofbooks = 0
        self.books = []
    
    def add_books(self, books):
        self.books.append(books)
        self.noofbooks = len(self.books)

    def show(self):
        print(f"This system has total {self.noofbooks} books and the Books are:")
        for book in self.books:
            print(book)


l1 = LibraryManagement()
l1.add_books("harrypotter1")
l1.show()
l1.add_books("harrypotter2")
l1.show()
l1.add_books("harrypotter3")
l1.show()
l1.add_books("harrypotter4")
l1.show()