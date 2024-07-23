def div():
    print('='*50)


def display_books(books):
    for book in books:
        div()
        print(f"Title: {book[1]}")
        print(f"Author: {book[0]}")
        div()

def add_to_library(books):
    author = input("What is the name of the author? ")
    title = input("what is the title of the book? ")
    book = [author, title]
    books.append(book)
    return books

def main():
    library = []
    flag = True
    while flag:
        ans = input('''
What would you like to do?
1 - Add a new book
2 - View all books
3 - Quit
''')
        
        if ans == '1':
            updated_library = add_to_library(library) # a function for adding a book
            library = updated_library
        elif ans == '2':
            display_books(library) # a function for viewing all books
        elif ans == '3':
            flag = False
            print("thanks for visiting our library!")

main()