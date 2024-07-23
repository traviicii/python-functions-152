def div():
    print('='*50)


# In python we have two different types of scope. Global scope and local scope

# the scope determines what variables are accessible

# Global scope is anywhere outside of a function or a for loop

# Global Variable
x = 7 # Variables defined on a global scope can be accessed from anywhere within our code
a = "Words"
alist = ["item1", "item2", "item3"]

if x:
    print(x)

# Local scope is created inside of a function (or a for loop)

def local_func():
    y = 10 # local variable, only accessible inside of this function

    print(x)

local_func()
# print(y)

books = [] # defined on a global scope. this library of books can be accessed anywhere in this file

def add_to_library(author, title):
    book = [author, title] # defined on a local scope and only available inside of this function
    books.append(book)

add_to_library("J.K. Rowling", "Harry Potter and the Deathly Hallows")
add_to_library("Neil Geiman", "Smoke and Mirrors")

def display_books():
    for book in books:
        div()
        print(f"Title: {book[1]}")
        print(f"Author: {book[0]}")
        div()

display_books()