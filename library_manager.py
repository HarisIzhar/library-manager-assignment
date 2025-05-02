import os
import json

def load_library():
    if os.path.exists("library.txt"):
        with open("library.txt", "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_library(library):
    with open("library.txt", "w") as file:
        json.dump(library, file)

def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("Invalid year. Book not added.")
        return
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)
    print("Book added successfully!")

def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

def search_book(library):
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")
    query = input("Enter your search term: ").lower()

    found = []
    for book in library:
        if choice == "1" and query in book["title"].lower():
            found.append(book)
        elif choice == "2" and query in book["author"].lower():
            found.append(book)

    if found:
        print("Matching Books:")
        for idx, book in enumerate(found, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")

def display_all_books(library):
    if not library:
        print("Your library is empty.")
        return
    print("Your Library:")
    for idx, book in enumerate(library, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

def display_stats(library):
    total = len(library)
    if total == 0:
        print("No books in library.")
        return
    read_books = sum(1 for book in library if book["read"])
    percent_read = (read_books / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percent_read:.1f}%")

def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()