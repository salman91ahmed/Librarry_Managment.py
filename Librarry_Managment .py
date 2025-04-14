# Logic Wala Kaam

# list_of_books 
list_of_books = []

# Adding Function 
def adding():
    booktitle = str(input("Enter the book title: ").lower())
    author = str(input("Enter the author: ").lower())
    publication = str(input("Enter the publication year: ").lower())
    genre = str(input("Enter the genre: ").lower())
    read = str(input("Have you read this book? (yes/no): ").lower()) == "yes"

    adding_book = {
        'bookTitle': booktitle,
        'author': author,
        'publication': publication,
        'genre': genre,
        'read': read
    }
    list_of_books.append(adding_book)
    print("Book added successfully!")

# Removing Function
def removing():
    removing_book = str(input("Enter the book title you want to remove: ").lower())
    for i in list_of_books:
        if i['bookTitle'] == removing_book:
            list_of_books.remove(i)
            print("Book removed successfully!")
            return
    print("Book not found!")

# Searching Function
def searching():
    userinput = str(input('Enter the book title you want to search: ').lower())
    for i in list_of_books:
        if i['bookTitle'] == userinput:
            print(i)
            return
    print("Book not found!")

# Display All Books
def display_all_books():
    if not list_of_books:
        print("No books in the library.")
    else:
        for book in list_of_books:
            print(book)

# Main Program Loop
while True:
    print('''
Welcome to your Personal Library Manager!  
1. Add a book  
2. Remove a book  
3. Search for a book  
4. Display all books  
5. Exit  
''')

    userinput = int(input("Enter your choice: "))

    if userinput == 1:
        adding()
    elif userinput == 2:
        removing()
    elif userinput == 3:
        searching()
    elif userinput == 4:
        display_all_books()
    elif userinput == 5:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid Input")

    # Ask user if they want to continue
    continue_choice = input("Do you want to continue? (ok to continue, no to exit): ").lower()
    if continue_choice == "no":
        print("Exiting the program. Goodbye!")
        break