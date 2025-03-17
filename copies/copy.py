# import streamlit as st
# import json
# import os
# st.set_page_config(
#     page_title="Personal Library Manager",
#     page_icon="📚",
#     layout="centered",
#     initial_sidebar_state="expanded",
# )
# # JSON File Handling
# file = "library.json"
# if os.path.exists(file):
#     try:
#         with open(file, "r") as read_file:
#             library = json.load(read_file)
#     except (json.JSONDecodeError, FileNotFoundError):
#         library = []
# else:
#     library = []
# def save_library():
#     with open(file, "w") as write_file:
#         json.dump(library, write_file, indent=4)
# # Streamlit UI
# st.title("📚 Personal Library Manager")
# menu = st.sidebar.selectbox("Choose an action:", ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Statistics"])
# if menu == "Add a Book":
#     st.header("➕ Add a New Book")
#     title = st.text_input("Enter the book title:")
#     author = st.text_input("Enter the author's name:")
#     year = st.number_input("Enter the publication year:", min_value=200, max_value=9999, step=1,)
#     genre = st.text_input("Enter the genre:")
#     is_read = st.radio("Have you read this book?", ["Yes", "No"])
    
#     if st.button("Add Book"):
#         if title and author:
#             library.append({
#                 "title": title,
#                 "author": author,
#                 "year": year,
#                 "genre": genre,
#                 "is_read": is_read
#                 })
#             save_library()
#             st.success("✅ Book added successfully!")
#         else:
#             st.warning("⚠️ Please enter both title and author.")
# elif menu == "Remove a Book":
#     st.header("❌ Remove a Book")
#     book_titles = [book["title"] for book in library]
#     book_to_remove = st.selectbox("Select a book to remove:", book_titles)
    
#     if st.button("Remove Book"):
#         library[:] = [book for book in library if book["title"] != book_to_remove]
#         save_library()
#         st.success("✅ Book removed successfully!")

# elif menu == "Search for a Book":
#     st.header("🔍 Search for a Book")
#     search_query = st.text_input("Enter the book title or author:")
    
#     if st.button("Search"):
#         results = [book for book in library if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]
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

# elif menu == "Display All Books":
#     st.header("📚 All Books in the Library")
#     if library:
#         for book in library:
#             st.write(f"**📖 Title:** {book['title']}")
#             st.write(f"**👤 Author:** {book['author']}")
#             st.write(f"**📅 Year:** {book['year']}")
#             st.write(f"**📚 Genre:** {book['genre']}")
#             st.write(f"**✅ Read:** {book['is_read']}")
#             st.write("---")
#     else:
#         st.warning("❌ No books found in the library.")

# elif menu == "Statistics":
#     st.header("📊 Library Statistics")
#     total_books = len(library)
#     read_books = sum(1 for book in library if book["is_read"].lower() == "yes")
#     unread_books = total_books - read_books
    
#     st.write(f"📚 **Total books:** {total_books}")
#     st.write(f"✅ **Books read:** {read_books}")
#     st.write(f"📖 **Books unread:** {unread_books}")
    
#     if total_books > 0:
#         st.write(f"📈 **Percentage read:** {(read_books / total_books) * 100:.2f}%")
#     else:
#         st.warning("⚠️ No books available to calculate (Percentage).")





import streamlit as st
import json
import os

st.set_page_config(
    page_title="Personal Library Manager",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="expanded",
)

# JSON File Handling
file = "library.json"
if os.path.exists(file):
    try:
        with open(file, "r") as read_file:
            library = json.load(read_file)
    except (json.JSONDecodeError, FileNotFoundError):
        library = []
else:
    library = []

def save_library():
    with open(file, "w") as write_file:
        json.dump(library, write_file, indent=4)

# Initialize session state for input fields
if 'title' not in st.session_state:
    st.session_state.title = ""
if 'author' not in st.session_state:
    st.session_state.author = ""
if 'year' not in st.session_state:
    st.session_state.year = 200
if 'genre' not in st.session_state:
    st.session_state.genre = ""
if 'is_read' not in st.session_state:
    st.session_state.is_read = "No"

# Streamlit UI
st.title("📚 Personal Library Manager")

menu = st.sidebar.selectbox("Choose an action:", ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Statistics"])

if menu == "Add a Book":
    st.header("➕ Add a New Book")
    st.session_state.title = st.text_input("Enter the book title:", value=st.session_state.title)
    st.session_state.author = st.text_input("Enter the author's name:", value=st.session_state.author)
    st.session_state.year = st.number_input("Enter the publication year:", min_value=200, max_value=9999, step=1, value=st.session_state.year)
    st.session_state.genre = st.text_input("Enter the genre:", value=st.session_state.genre)
    st.session_state.is_read = st.radio("Have you read this book?", ["Yes", "No"], index=0 if st.session_state.is_read == "Yes" else 1)
    
    if st.button("Add Book"):
        if st.session_state.title and st.session_state.author:
            library.append({
                "title": st.session_state.title,
                "author": st.session_state.author,
                "year": st.session_state.year,
                "genre": st.session_state.genre,
                "is_read": st.session_state.is_read
                })
            save_library()
            st.success("✅ Book added successfully!")
            # Clear input fields
            st.session_state.title = ""
            st.session_state.author = ""
            st.session_state.year = 2000
            st.session_state.genre = ""
            st.session_state.is_read = "No"
        else:
            st.warning("⚠️ Please enter both title and author.")

elif menu == "Remove a Book":
    st.header("❌ Remove a Book")
    book_titles = [book["title"] for book in library]
    book_to_remove = st.selectbox("Select a book to remove:", book_titles)
    
    if st.button("Remove Book"):
        library[:] = [book for book in library if book["title"] != book_to_remove]
        save_library()
        st.success("✅ Book removed successfully!")

elif menu == "Search for a Book":
    st.header("🔍 Search for a Book")
    search_query = st.text_input("Enter the book title or author:")
    
    if st.button("Search"):
        results = [book for book in library if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]
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

elif menu == "Display All Books":
    st.header("📚 All Books in the Library")
    if library:
        for book in library:
            st.write(f"**📖 Title:** {book['title']}")
            st.write(f"**👤 Author:** {book['author']}")
            st.write(f"**📅 Year:** {book['year']}")
            st.write(f"**📚 Genre:** {book['genre']}")
            st.write(f"**✅ Read:** {book['is_read']}")
            st.write("---")
    else:
        st.warning("❌ No books found in the library.")

elif menu == "Statistics":
    st.header("📊 Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book["is_read"].lower() == "yes")
    unread_books = total_books - read_books
    
    st.write(f"📚 **Total books:** {total_books}")
    st.write(f"✅ **Books read:** {read_books}")
    st.write(f"📖 **Books unread:** {unread_books}")
    
    if total_books > 0:
        st.write(f"📈 **Percentage read:** {(read_books / total_books) * 100:.2f}%")
    else:
        st.warning("⚠️ No books available to calculate (Percentage).")