# import streamlit as st
# from pymongo import MongoClient 
# from dotenv import load_dotenv
# import os
# import certifi


# # Load environment variables
# load_dotenv()
# MONGO_URI = os.getenv("MONGO_URI") or "mongodb+srv://rk8466995:cJ4PvAFk6nvhKaQM@cluster0.cjede.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Connect to MongoDB
# client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
# db = client["library_manager"]
# books_collection = db["books"]

# # Streamlit UI Setup
# st.set_page_config(page_title="📚 Personal Library Manager", page_icon="📖", layout="centered")
# st.title("📖 Personal Library Manager")

# # Book Management UI
# menu = st.sidebar.selectbox("Choose an action:", ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Statistics"])

# # ➕ Add a Book
# if menu == "Add a Book":
#     st.header("➕ Add a New Book")
#     title = st.text_input("Book Title")
#     author = st.text_input("Author")
#     year = st.number_input("Publication Year", min_value=1900, max_value=9999, step=1)
#     genre = st.text_input("Genre")
#     is_read = st.radio("Have you read it?", ["Yes", "No"])
    
#     if st.button("Add Book"):
#         books_collection.insert_one({
#             "title": title,
#             "author": author,
#             "year": year,
#             "genre": genre,
#             "is_read": is_read
#         })
#         st.success("✅ Book added successfully!")

# # ❌ Remove a Book
# elif menu == "Remove a Book":
#     st.header("❌ Remove a Book")
#     books = list(books_collection.find())
#     book_titles = [book["title"] for book in books]

#     if book_titles:
#         book_to_remove = st.selectbox("Select a book to remove:", book_titles)
#         if st.button("Remove Book"):
#             books_collection.delete_one({"title": book_to_remove})
#             st.success("✅ Book removed successfully!")
#             st.rerun()
#     else:
#         st.warning("⚠️ No books found to remove.")

# # 🔍 Search for a Book
# elif menu == "Search for a Book":
#     st.header("🔍 Search for a Book")
#     search_query = st.text_input("Enter the book title or author:")
    
#     if st.button("Search"):
#         results = books_collection.find({
#             "$or": [
#                 {"title": {"$regex": search_query, "$options": "i"}},
#                 {"author": {"$regex": search_query, "$options": "i"}}
#             ]
#         })
        
#         results = list(results)
#         if results:
#             for book in results:
#                 st.write(f"**📖 Title:** {book['title']}")
#                 st.write(f"**👤 Author:** {book['author']}")
#                 st.write(f"**📅 Year:** {book['year']}")
#                 st.write(f"**📚 Genre:** {book['genre']}")
#                 st.write(f"**✅ Read:** {book['is_read']}")
#                 st.write("---")
#         else:
#             st.warning("❌ No book found!")

# # 📚 Display All Books
# elif menu == "Display All Books":
#     st.header("📚 All Books in the Library")
#     books = books_collection.find()

#     books = list(books)
#     if books:
#         for book in books:
#             st.write(f"**📖 Title:** {book['title']}")
#             st.write(f"**👤 Author:** {book['author']}")
#             st.write(f"**📅 Year:** {book['year']}")
#             st.write(f"**📚 Genre:** {book['genre']}")
#             st.write(f"**✅ Read:** {book['is_read']}")
#             st.write("---")
#     else:
#         st.warning("❌ No books found in the library.")

# # 📊 Library Statistics
# elif menu == "Statistics":
#     st.header("📊 Library Statistics")
#     books = list(books_collection.find())
    
#     total_books = len(books)
#     read_books = sum(1 for book in books if book["is_read"].lower() == "yes")
#     unread_books = total_books - read_books
    
#     st.write(f"📚 **Total books:** {total_books}")
#     st.write(f"✅ **Books read:** {read_books}")
#     st.write(f"📖 **Books unread:** {unread_books}")
    
#     if total_books > 0:
#         st.write(f"📈 **Percentage read:** {(read_books / total_books) * 100:.2f}%")
#     else:
#         st.warning("⚠️ No books available to calculate (Percentage).")


import streamlit as st
from pymongo import MongoClient 
from dotenv import load_dotenv
import bcrypt
import os

# Load environment variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI") or "mongodb+srv://rk8466995:cJ4PvAFk6nvhKaQM@cluster0.cjede.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["library_manager"]
users_collection = db["users"]
books_collection = db["books"]

# Streamlit UI Setup
st.set_page_config(page_title="📚 Personal Library Manager", page_icon="📖", layout="centered")

# User Authentication Functions
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

def create_user(username, password):
    if users_collection.find_one({"username": username}):
        return False
    hashed_password = hash_password(password)
    users_collection.insert_one({"username": username, "password": hashed_password})
    return True

def authenticate_user(username, password):
    user = users_collection.find_one({"username": username})
    if user and check_password(password, user["password"]):
        return True
    return False

# Session State for Authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Authentication UI
st.title("📖 Personal Library Manager")
if not st.session_state.authenticated:
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        st.subheader("🔑 Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if authenticate_user(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.success("✅ Login successful!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")
    
    with tab2:
        st.subheader("🆕 Sign Up")
        new_username = st.text_input("Choose a Username")
        new_password = st.text_input("Choose a Password", type="password")
        if st.button("Sign Up"):
            if create_user(new_username, new_password):
                st.success("✅ Account created! Please login.")
            else:
                st.warning("⚠️ Username already taken.")
else:
    st.sidebar.write(f"👤 Logged in as **{st.session_state.username}**")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.username = ""
        st.rerun()
    
    st.write("### 📚 Welcome to Your Personal Library")
    
    # Book Management UI
    menu = st.sidebar.selectbox("Choose an action:", ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Statistics"])

    # ➕ Add a Book
    if menu == "Add a Book":
        st.header("➕ Add a New Book")
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        year = st.number_input("Publication Year", min_value=1000, max_value=9999, step=1)
        genre = st.text_input("Genre")
        is_read = st.radio("Have you read it?", ["Yes", "No"])
        
        if st.button("Add Book"):
            books_collection.insert_one({
                "username": st.session_state.username,
                "title": title,
                "author": author,
                "year": year,
                "genre": genre,
                "is_read": is_read
            })
            st.success("✅ Book added successfully!")

    # ❌ Remove a Book
    elif menu == "Remove a Book":
        st.header("❌ Remove a Book")
        books = list(books_collection.find({"username": st.session_state.username}))
        book_titles = [book["title"] for book in books]

        if book_titles:
            book_to_remove = st.selectbox("Select a book to remove:", book_titles)
            if st.button("Remove Book"):
                books_collection.delete_one({"username": st.session_state.username, "title": book_to_remove})
                st.success("✅ Book removed successfully!")
                st.rerun()
        else:
            st.warning("⚠️ No books found to remove.")

    # 🔍 Search for a Book
    elif menu == "Search for a Book":
        st.header("🔍 Search for a Book")
        search_query = st.text_input("Enter the book title or author:")
        
        if st.button("Search"):
            results = books_collection.find({
                "username": st.session_state.username,
                "$or": [
                    {"title": {"$regex": search_query, "$options": "i"}},
                    {"author": {"$regex": search_query, "$options": "i"}}
                ]
            })
            
            results = list(results)
            if results:
                for book in results:
                    st.write(f"**📖 Title:** {book['title']}")
                    st.write(f"**👤 Author:** {book['author']}")
                    st.write(f"**📅 Year:** {book['year']}")
                    st.write(f"**📚 Genre:** {book['genre']}")
                    st.write(f"**✅ Read:** {book['is_read']}")
                    st.write("---")
            else:
                st.warning("❌ No book found!")

    # 📚 Display All Books
    elif menu == "Display All Books":
        st.header("📚 All Books in the Library")
        books = books_collection.find({"username": st.session_state.username})

        books = list(books)
        if books:
            for book in books:
                st.write(f"**📖 Title:** {book['title']}")
                st.write(f"**👤 Author:** {book['author']}")
                st.write(f"**📅 Year:** {book['year']}")
                st.write(f"**📚 Genre:** {book['genre']}")
                st.write(f"**✅ Read:** {book['is_read']}")
                st.write("---")
        else:
            st.warning("❌ No books found in the library.")

    # 📊 Library Statistics
    elif menu == "Statistics":
        st.header("📊 Library Statistics")
        books = list(books_collection.find({"username": st.session_state.username}))
        
        total_books = len(books)
        read_books = sum(1 for book in books if book["is_read"].lower() == "yes")
        unread_books = total_books - read_books
        
        st.write(f"📚 **Total books:** {total_books}")
        st.write(f"✅ **Books read:** {read_books}")
        st.write(f"📖 **Books unread:** {unread_books}")
        
        if total_books > 0:
            st.write(f"📈 **Percentage read:** {(read_books / total_books) * 100:.2f}%")
        else:
            st.warning("⚠️ No books available to calculate (Percentage).")
