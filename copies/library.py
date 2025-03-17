import json
import os

file = "library.json"

if os.path.exists(file):
    try:
        with open(file, "r") as read_file:
            library = json.load(read_file)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
        library = []
else:
    library = []
    
    

    print("Welcome to your Personal Library Manager!")
    print("\n1. Add a book ")
    print("2. Remove a book ")
    print("3. Search for a book ")
    print("4. Display all books ")
    print("5. Display statistics ")
    print("6. Exit")


menu = int(input("Enter your desired choice: "))

if menu == 1:
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    is_read = input("Have you read this book? (yes/no): ")
    
    
    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "is_read": is_read
    })
    
    
    with open(file, "w") as file_data:
        json.dump(library, file_data, indent=4)
    
    print("Book added successfully!")
    
elif menu == 2:
    
    title = input("Enter the title or author of the book you want to remove: ")
    
    for book in library:
        
        if book["title"] == title or book["author"] == title:
            library.remove(book)
            
            with open(file, "w") as remove_book:
                json.dump(library, remove_book, indent=4)
                print("Book removed successfully!") 
        
    print("Book not found in the library.")
        
elif menu == 3:
    
    title = input("Enter the title or the author of the book: ")
    for book in library:
        if book["title"] == title or book["author"] == title:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Publication Year: {book['year']}")
            print(f"Genre: {book['genre']}")
            print(f"Has been read: {book['is_read']}")
    else:
        print("Invalid search option, book not found")
            
elif menu == 4:
    print("All books in the library:")
    print("--------------------")
    if library:
        for book in library:
            print(f"\nTitle: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Publication Year: {book['year']}")
            print(f"Genre: {book['genre']}")
            print(f"Has been read: {book['is_read']}")
            print("--------------------")
    else:
        print("No books found in the library.")
        
elif menu == 5:
    total_books = len(library)
    read_books = sum(1 for book in library if book["is_read"] == "yes")
    unread_books = total_books - read_books
    
    print(f"Total books in the library: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Books unread: {unread_books}")
    print(f"Percentage of books read: {(read_books / total_books) * 100:.2f}%")
    
    if total_books == 0:
        print("No books found in the library, please try again.")
    
elif menu == 6:
    print("Thank you for using the Personal Library Manager! (You Clicked on Quit Button)")
    
else:
    print("Invalid choice, please try again.")
    
     