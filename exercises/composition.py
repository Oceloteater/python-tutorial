class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f'Bookshelf with {len(self.books)} books.'

    def get_books(self):
        for book in self.books:
            print(book)


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'


book = Book('Harry Pothead')
book2 = Book('Harry Headpotter')
shelf = BookShelf(book, book2)

print(shelf)
shelf.get_books()
