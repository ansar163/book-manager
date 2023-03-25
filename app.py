import json

class BookDetails:
    def __init__(self, id, title, author, year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year

# Returns list of books ID
def getBooksId(filename):
    listOfIds = []
    # Load current- book data.
    with open(filename, 'r') as file:
        bookFile = json.load(file)
    # Gets book IDs in a list.
    for book in bookFile['books']:
        listOfIds.append(book['id'])
    return listOfIds

# Add a book.
def addBook():
    id = input('Enter the id of the book: ')
    title = input('Enter the title of the book: ')
    author = input('Enter the name of the author: ')
    try:
        year = int(input('Enter the year of publication: '))
    except:
        print()
        print('Failed to add a book')
        print('Year is not an integer')
        return
    # Instance of class BookDetails
    book = BookDetails(id, title, author, year)
    # Loads JSON file, add a new book and store it locally
    # Overwrite the JSON file with the stored data.
    with open('books.json','r+') as file:
        bookFile = json.load(file)
        bookFile['books'].append(book.__dict__)
        file.truncate(0)
        file.seek(0)
        json.dump(bookFile, file, indent = 4)
    print()
    print('Book added successfully !')

# Titles of books.
def getTitleOfBooks():
    # Load current books data.
    with open('books.json', 'r') as file:
        books = json.load(file)
    # Count of books.
    bookCount = len(books['books'])
    # Pagination.
    pageNumber = 1
    print("Number of book titles found: ", bookCount)
    print()
    while True:
        bookCount -= 10
        startIndex = (pageNumber - 1) * 10
        endIndex = startIndex + 10
        # Display title of books based on pagination.
        for book in books['books'][startIndex:endIndex]:
            print(book['title'])
        # If next page exists, trigger it once pressed 'n'
        if bookCount >= 0:
            nextPage = input("Press 'n' to get next page's list or any key to exit: ")
            if nextPage == 'n':
                pageNumber += 1
            else:
                break
        else:
            break

# Update an existing book details
def updateBook():
    id = input("Enter the ID of book that you want to update: ")
    listOfId = getBooksId('books.json')
    if id in listOfId:
        newTitle = input("Enter the title of the book to update: ")
        newAuthor = input("Enter the name of the author to update: ")
        try:
            newYear = int(input("Enter the year of publication to update: "))
        except:
            print()
            print('Failed to update a book')
            print('Year is not an integer')
            return
        # Loads JSON file, update the required book and store it locally
        # Overwrite the JSON file with the stored data.
        with open('books.json', 'r+') as file:
            bookFile = json.load(file)
            # Instance of class BookDetails
            updatedBook = BookDetails(id, newTitle, newAuthor, newYear)
            for i in range(len(bookFile['books'])):
                if bookFile['books'][i]['id'] == id:
                    bookFile['books'][i] = updatedBook.__dict__
                    break
            file.truncate(0) 
            file.seek(0)
            json.dump(bookFile, file, indent = 4)
        print()
        print('Book details updated successfully !')
    else:
        print()
        print(f'Entered ID "{id}" does not exists !')

# Delete a book
def deleteBook():
    id = input("Enter the ID of book that you want to update: ")
    listOfId = getBooksId('books.json')
    if id in listOfId:
        # Loads JSON file, delete the required book using it's ID and store it locally
        # Overwrite the JSON file with the stored data.
        with open('books.json', 'r+') as file:
            bookFile = json.load(file)
            for book in bookFile['books']:
                if book['id'] == id:
                    bookFile['books'].remove(book)
                    break
            file.truncate(0)
            file.seek(0)
            json.dump(bookFile, file, indent = 4)
        print()
        print('Book deleted successfully !')
    else:
        print()
        print(f'Entered ID "{id}" does not exists !')

# Display all authors.
def getAuthorsName():
    # List of authors to get unique author name.
    authors = set()
    # Load current book data.
    with open('books.json', 'r') as file:
        bookFile = json.load(file)
    # Add author names in authors list from books.
    for book in bookFile['books']:
        authors.add(book['author'])
    print("Count of authors fetched: ", len(authors))
    print()
    # Display all fetched author names
    for author in authors:
        print(author)

# Map choice with respective functionality.
mapToFunctionality = {
    1: addBook,
    2: getTitleOfBooks,
    3: updateBook,
    4: deleteBook,
    5: getAuthorsName,
}

while True:
    print("------------------------------------------------------")
    print("Choose one of the following:")
    print("1. Add a book")
    print("2. List all title of books")
    print("3. Update a book")
    print("4. Delete a book")
    print("5. List all authors")
    print('6. Exit program')
    print("------------------------------------------------------")

    # Gets selected choice from user
    inputChoice = int(input('Enter choice: '))

    # Exit the program
    if inputChoice == 6:
        break

    # Gets function to be executed on selected choice.
    selectedChoiceFunction = mapToFunctionality.get(inputChoice)

    # Executes the function.
    try:
        selectedChoiceFunction()
    except:
        print()
        print('Invalid choice')
