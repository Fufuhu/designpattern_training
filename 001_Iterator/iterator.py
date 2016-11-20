class Iterator:
    def has_next(self):
         return True
    def next(self):
         return None

class Aggregator:
    def iterator(self):
        return None

class Book:
    def __init__(self, name):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    name = property(get_name, set_name)

class BookShelf(Aggregator):
    def __init__(self):
        self.__books = []

    def get_book_at(self, index):
        return self.__books[index]
    
    def append_book(self, name):
        book = Book(name)
        self.__books = self.__books + [book]
    
    def get_length(self):
        return len(self.__books)
    
    def iterator(self):
        return BookShelfIterator(self)

class BookShelfIterator(Iterator):
    def __init__(self, bookshelf):
        self.__bookshelf = bookshelf
        self.__index = 0
    
    def has_next(self):
        if self.__index < self.__bookshelf.get_length():
            return True
        else:
            return False
    
    def next(self):
        self.__index += 1
        return self.__bookshelf.get_book_at(self.__index - 1)

bookshelf = BookShelf()
bookshelf.append_book("Around the world in 80 days")
bookshelf.append_book("Bible")
bookshelf.append_book("Cinderella")
bookshelf.append_book("Daddy-Long-Legs")

it = bookshelf.iterator()


while it.has_next():
   book = it.next()
   print(book.name)


