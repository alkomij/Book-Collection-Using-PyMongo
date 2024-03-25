from models.book import Book

class BookService:

    # addBook()
    @staticmethod
    def addBook(book_data):
        book = Book(**book_data)
        book.save()
        return book

    # getAllBooks()
    @staticmethod
    def getAllBooks():
        books = Book.objects.All()
        return books

    # getBookById()
    @staticmethod
    def getBookById(book_id):
        booksId = Book.objects.get(id=book_id)
        return booksId
    
    # updateBook()
    @staticmethod
    def updateBook(book_id, update_data):
        book = Book.objects(id=book_id).update_one(**update_data)
        return book
        
    # deleteBook()
    @staticmethod
    def deleteBook(book_id):
        result = Book.objects(id=book_id).delete()
        return result

