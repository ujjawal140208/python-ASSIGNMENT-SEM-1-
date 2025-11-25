# Library Inventory Manager  
A simple, human-friendly Python project that manages books using Object-Oriented Programming (OOP) and JSON storage.

This is a command-line based mini-project where you can:

- Add new books  
- Issue books  
- Return books  
- Search books  
- View all books  
- Save all data automatically to a JSON file  

Everything is designed to be simple, readable, and beginner-friendly.

---

# How the Project Works

The project is made of **three main files**:
1. `book.py` — The “Book” Blueprint

This file defines the `Book` class.

A book has:
- a title  
- an author  
- an ISBN (unique ID)  
- a status → “available” or “issued”  

### Main functions inside:
- `__init__()` → creates a book  
- `__str__()` → how a book looks when printed  
- `to_dict()` → convert to dictionary (for JSON)  
- `from_dict()` → recreate a book from dictionary  
- `issue()` → mark as issued  
- `return_book()` → mark as available  
- `is_available()` → check if book is available  

This keeps all book-related logic clean and organized.

---

2. `inventory.py` — Manages the Entire Library

This file contains the **LibraryInventory** class.

It:
- stores a list of all books  
- loads/saves books from/to `books.json`  
- adds new books  
- issues or returns books  
- searches books by title or ISBN  

### Important functions:
- `load()` → reads JSON file  
- `save()` → writes JSON file  
- `add_book()` → adds book (only if ISBN is unique)  
- `find_by_isbn()` → find exact ISBN  
- `find_by_title()` → partial search  
- `issue_book()` → change status to “issued”  
- `return_book()` → change status to “available”  

This class is like the “brain” of the library system.


 3. `main.py` — The User Interface (CLI)

This is the file you actually run.



