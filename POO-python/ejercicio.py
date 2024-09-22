class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.available = True

  def borro(self):
    if self.available:
      self.available = False
      print(f"El libro {self.title} ha sido prestado")

    else: 
      print(f"El libro {self.title} no es esta disponible")

  def return_book(self):
    self.available = True
    print(f"El libro  {self.title} ha sido devuelto")

class User:
  def __init__(self, name, user_id):
    self.name = name
    self.user_id = user_id
    self.borrowe_books = []

  def borrow_book(self, book):
    if book.available:
      book.boroow()
      self.borrowe_books.append(book)
    else:
      print(f"el libro {book.title} No esta disponible")
  
  def return_book (self, book):
    if book in self.borrowe_books:
      book.return_book()
      self.borrowe_books.remove(book)
    else:
      print(f"El libro {book.title} No esta en la lista de prestamos")

class Library:
  def __init__(self):
    self.books = []
    self.users = []

  def add_book(self, book):
      self.books.append(book)
      print(f"el libro {book.title} Ha sido Asignado")
  def register_user (self, user):
      self.users.append(user)
      print(f"El usuario {user.name} ha sido registrado")
  def show_available_books (self):
      print("Libros disponibles:")
      for book in self.add_book:
        if book.available:
          print(f"{book.title} por {book.author}")

#crear los libros
book1 = Book("El principito ", "Antoine de Saint-Exupe")
book2 = Book("1984", "Geoge Orwell")

#crear usuarios

user1 = User("Carli", "001")

#crear biblioteca

library = Library ()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

#mostrar libros

library.show_available_books()

#realizar prestamos

user1.borrow_book(book1)

user1.return_book(book1)
