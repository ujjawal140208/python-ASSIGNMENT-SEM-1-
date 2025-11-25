from library_manager.inventory import LibraryInventory

lib = LibraryInventory()

def menu():
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        t = input("Title: ")
        a = input("Author: ")
        i = input("ISBN: ")
        ok = lib.add_book(t, a, i)
        print("Book added!" if ok else "ISBN already exists!")

    elif choice == "2":
        i = input("Enter ISBN to issue: ")
        ok = lib.issue_book(i)
        print("Issued!" if ok else "Cannot issue.")

    elif choice == "3":
        i = input("Enter ISBN to return: ")
        ok = lib.return_book(i)
        print("Returned!" if ok else "Cannot return.")

    elif choice == "4":
        print("\n--- All Books ---")
        for b in lib.books:
            print(b)

    elif choice == "5":
        q = input("Search title: ")
        results = lib.find_by_title(q)
        if results:
            for r in results:
                print(r)
        else:
            print("No books found.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
# End of main.py