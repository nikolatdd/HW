class Library():
    books = list()
    def __init__(self,name):
        self.library_name=name
    def add_book(self):
        if isinstance(self, Books):
            Library.books.append(self.__dict__)
        else:
            print('Must be book')

    @staticmethod
    def search_by_author(desired_author):  
        for b in Library.books:
            for key,val in b.items():                
                if key == 'author' and val == desired_author:
                    title = b['title']
                    print(f'{title} - {desired_author}')
    @staticmethod                 
    def book_info():
        desired_book = str(input('Title of the book to get information on it: '))
        for b in Library.books:
            for key,val in b.items():
                if key == 'title' and val == desired_book:
                    print(f'Book found:')
                    for key,val in b.items():
                        print(f'{key} --> {val}''')
    @staticmethod                    
    def delete_book():
        book_to_delete = str(input('Title of the book to delete: '))
        for b in Library.books:
            for key,val in b.items():
                if key == 'title' and val == book_to_delete:
                    print(f'Deleting book - {val}')
                    Library.books.remove(b)
    @staticmethod                
    def list_books():
        status = Library.books
        if not Library.books:
            status = None
        print(f'List of the books: {status}')

class Books(Library):   
    def __init__(self,title,author,publisher,year: int,isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.release_year = year
        self.ISBN = isbn

book1 = Books('Harry Potter', 'J.K Rowling', None, 1991, '0-6910-7897-1')
book1.add_book()
# Library.search_by_author('J.K Rowling')
# Library.book_info()
Library.delete_book()
Library.list_books()