
# Zanetta Recendez, IS-31

# Store book titles and control the menu loop.
books = []
running = True

print("Welcome to your library!")

while running:
    # Display the menu and get the user's choice.
    print("\n1. Add a book")
    print("2. Quit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        # Ask for a title and add it to the list.
        title = input("Enter the book title: ")
        books.append(title)
        print("Book added!")

    elif choice == "2":
        # Stop the loop.
        running = False

    else:
        # Guide the user back to the valid options.
        print("Invalid choice. Please enter 1 or 2.")

# Display the books after the user quits.
print("\nThank you for using your library!")
print("Books in your library:")

for book in books:
    print(book)