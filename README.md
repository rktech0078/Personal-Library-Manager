# Personal Library Manager

## Overview
The **Personal Library Manager** is a user-friendly application built with **Streamlit** that helps users manage their personal book collection efficiently. The application allows users to add, remove, search, and display books while also providing useful reading statistics.

## Features
- 📖 **Add a Book**: Users can input book details such as title, author, publication year, genre, and reading status.
- ❌ **Remove a Book**: Select and delete a book from the library.
- 🔍 **Search for a Book**: Find books based on title or author.
- 📚 **Display All Books**: View all books currently stored in the library.
- 📊 **Library Statistics**: Get insights into the number of books read and unread.

## Technologies Used
- **Python** (Programming Language)
- **Streamlit** (For Web Interface)
- **JSON** (For Data Storage)
- **OS Module** (For File Handling)

## Installation
To use the Personal Library Manager, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/rktech0078/Personal-Library-Manager
   cd personal-library-manager
   ```

2. **Install Dependencies:**
   ```sh
   pip install streamlit
   ```

3. **Run the Application:**
   ```sh
   streamlit run app.py
   ```

4. **Also Check in this Link**
    https://rafay-library-manager.streamlit.app/

## How It Works
### Adding a Book
- Navigate to the "Add a Book" section.
- Enter the book's details.
- Click the **Add Book** button to save it.

### Removing a Book
- Go to "Remove a Book."
- Select a book from the dropdown list.
- Click **Remove Book** to delete it.

### Searching for a Book
- Navigate to "Search for a Book."
- Enter a book title or author's name.
- Click **Search** to see results.

### Displaying All Books
- Click on "Display All Books" to view the complete collection.

### Viewing Statistics
- Click "Statistics" to see:
  - Total books in the library.
  - Number of books read/unread.
  - Percentage of books read.

## Data Storage
All books are stored in a JSON file named **library.json**, ensuring persistent storage even after restarting the application.

## Future Improvements
- 📌 **Category Sorting**: Add the ability to filter books by genre.
- 📌 **Export to CSV**: Allow users to download their library data.
- 📌 **Cloud Storage Support**: Integrate with Google Drive or Firebase.

## License
This project is licensed under the **MIT License**.

---
🚀 Enjoy managing your book collection with **Personal Library Manager!**

