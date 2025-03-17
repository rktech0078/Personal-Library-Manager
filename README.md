# Personal Library Manager

## Overview
The **Personal Library Manager** is a web application built with **Streamlit** and **MongoDB** that allows users to manage their personal book collection. Users can securely log in, add books, remove books, search for books, and view insightful reading statistics.

## Features
- 🔑 **User Authentication**: Secure **Login** and **Signup** functionality to save user data.
- 📖 **Add a Book**: Users can add book details including title, author, publication year, genre, and reading status.
- ❌ **Remove a Book**: Select and delete books from the library.
- 🔍 **Search for a Book**: Find books based on title or author.
- 📚 **Display All Books**: View all books stored in the library.
- 📊 **Library Statistics**: Track books read, unread, and total count.

## Technologies Used
- **Python** (Programming Language)
- **Streamlit** (For Web Interface)
- **MongoDB** (For Data Storage)
- **PyMongo** (For Database Connection)
- **bcrypt** (For Password Hashing)
- **dotenv** (For Secure Environment Variables)

## Installation
To use the **Personal Library Manager**, follow these steps:

### 1️⃣ Clone the Repository:
```sh
git clone https://github.com/rktech0078/Personal-Library-Manager
cd Personal-Library-Manager
```

### 2️⃣ Install Dependencies:
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables:
Create a `.env` file and add your **MongoDB URI**:
```sh
MONGO_URI = "your-mongodb-connection-string"
```

### 4️⃣ Run the Application:
```sh
streamlit run app.py
```

### 5️⃣ Live Demo:
Check out the **live version** of the app:
🔗 [Personal Library Manager](https://db-library-manager.streamlit.app/)

## How It Works
### 🔐 User Authentication
- **Sign Up**: New users can create an account.
- **Login**: Existing users can log in to access their books.

### 📖 Adding a Book
- Navigate to the **"Add a Book"** section.
- Enter the book's details.
- Click **Add Book** to save it.

### ❌ Removing a Book
- Go to the **"Remove a Book"** section.
- Select a book from the list.
- Click **Remove Book** to delete it.

### 🔍 Searching for a Book
- Navigate to **"Search for a Book"**.
- Enter a book title or author's name.
- Click **Search** to find matching results.

### 📚 Displaying All Books
- Click **"Display All Books"** to see your entire library.

### 📊 Viewing Statistics
- Click **"Statistics"** to see:
  - Total number of books.
  - Number of books read/unread.
  - Percentage of books read.

## Future Improvements
- 📌 **Category Sorting**: Filter books by genre.
- 📌 **Export Data**: Allow users to download their book collection as a CSV.
- 📌 **Cloud Storage Support**: Integrate with Google Drive or Firebase for cloud storage.

## License
This project is licensed under the **MIT License**.

---
🚀 Start managing your personal library with **Personal Library Manager** today!

