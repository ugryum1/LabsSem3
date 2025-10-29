class Book:
    def __init__(self, id, title, author, pages, libraryID):
        self.id = id
        self.title = title
        self.author = author
        self.pages = pages
        self.libraryID = libraryID

class Library:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class BookLibrary:
    def __init__(self, libraryID, bookID):
        self.libraryID = libraryID
        self.bookID = bookID

books = [
    Book(1, "Преступление и наказание", "Достоевский", 350, 1),
    Book(2, "Война и мир", "Толстой", 1225, 2),
    Book(3, "Мастер и Маргарита", "Булгаков", 480, 2),
    Book(4, "Евгений Онегин", "Пушкин", 320, 4),
    Book(5, "Отцы и дети", "Тургенев", 288, 3),
    Book(6, "Герой нашего времени", "Лермонтов", 224, 1),
]

libraries = [
    Library(1, "Центральная городская библиотека"),
    Library(2, "Библиотека им. Ленина"),
    Library(3, "Научная библиотека"),
    Library(4, "Детская библиотека"),
]

booksLibraries = [
    BookLibrary(1, 1),
    BookLibrary(1, 6),
    BookLibrary(2, 2),
    BookLibrary(2, 3),
    BookLibrary(3, 4),
    BookLibrary(3, 5),
    BookLibrary(4, 1),
    BookLibrary(4, 2),
    BookLibrary(4, 3),
    BookLibrary(4, 4),
]


def main():
    oneToMany = [[book.title, book.author, book.pages, lib.name] for book in books for lib in libraries if book.libraryID == lib.id]

    print("Запрос 1")
    print("Список всех связанных книг и библиотек, отсортированный по книгам:")
    arr1 = sorted(oneToMany, key=lambda x: x[0])
    for i in arr1:
        print(f"Книга: {i[0]}, автор: {i[1]}, страниц: {i[2]}, библиотека: {i[3]}")


    print("\nЗапрос 2")
    print('Список библиотек с количеством книг в каждой, отсортированный по количеству книг (сначала, где меньше книг):')

    arr2 = []
    for lib in libraries:
        booksInLib = list(filter(lambda x: x[3] == lib.name, oneToMany))
        if len(booksInLib) > 0:
            arr2.append((lib.name, len(booksInLib)))

    arr2.sort(key=lambda x: x[1])
    for i in arr2:
        print(f"Библиотека: {i[0]}, количество книг: {i[1]}")


    print("\nЗапрос 3")
    print("Список всех книг, у которых автор заканчивается на 'ов', и названия их библиотек:")

    # через ключи
    manyToManyFirst = [[lib.name, bookInLib.libraryID, bookInLib.bookID] for lib in libraries for bookInLib in booksLibraries if lib.id == bookInLib.libraryID]

    # через названия
    manyToMany = [[book.title, book.author, book.pages, libName] for libName, libID, bookID in manyToManyFirst for book in books if book.id == bookID]

    arr3 = []
    for title, author, pages, libName in manyToMany:
        if author[-2:] == "ов":
            arr3.append([title, author, libName])

    arr3.sort(key=lambda x: x[0])
    for i in arr3:
        print(f"Книга: {i[0]}, автор: {i[1]}, библиотека: {i[2]}")

if __name__ == "__main__":
    main()
