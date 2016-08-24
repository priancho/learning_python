import book

class BookInventory:
    def __init__(self):
        self.books = list()             # All books in the inventory
    
    def size(self):
        return len(self.books)

    def add(self, book):
        self.books.append(book)

    def find(self, name):
        for book in self.books:
            if book.name == name:
                return book
        return None

    def get_all_books(self):
        return self.books


