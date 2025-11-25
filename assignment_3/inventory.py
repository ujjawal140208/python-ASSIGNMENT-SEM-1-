import json
from pathlib import Path
from .book import Book


class LibraryInventory:
    def __init__(self, file_path="books.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load()

    def load(self):
        if not self.file_path.exists():
            self.save()
            return

        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.books = [Book.from_dict(b) for b in data]

        except:
            self.books = []
            self.save()

    def save(self):
        with open(self.file_path, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=2)

    def add_book(self, title, author, isbn):
        if self.find_by_isbn(isbn):
            return False

        b = Book(title, author, isbn)
        self.books.append(b)
        self.save()
        return True

    def find_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def find_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def issue_book(self, isbn):
        b = self.find_by_isbn(isbn)
        if b:
            ok = b.issue()
            self.save()
            return ok
        return False

    def return_book(self, isbn):
        b = self.find_by_isbn(isbn)
        if b:
            ok = b.return_book()
            self.save()
            return ok
        return False
# End of library_manager/inventory.py