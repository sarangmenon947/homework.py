# Initialize the dictionary of textbooks and their costs
textbooks = {
    "math": 250,
    "physics": 300,
    "chemistry": 280
}

def display_menu():
    print("\nMenu:")
    print("1. Correct the cost of the Physics book")
    print("2. Add 2 more books to the dictionary")
    print("3. Print the cost of a specific book")
    print("4. Print all books and their costs")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        # Correct the cost of the Physics book
        textbooks["physics"] = 200
        print("The cost of the Physics book has been corrected to 200.")
    
    elif choice == "2":
        # Add 2 more books to the dictionary
        book1 = input("Enter the name of the first book: ").lower()
        cost1 = int(input(f"Enter the cost of {book1}: "))
        textbooks[book1] = cost1

        book2 = input("Enter the name of the second book: ").lower()
        cost2 = int(input(f"Enter the cost of {book2}: "))
        textbooks[book2] = cost2

        print("Two more books have been added to the dictionary.")
    
    elif choice == "3":
        # Print the cost of a specific book
        book = input("Enter the name of the book: ").lower()
        if book in textbooks:
            print(f"The cost of the {book} book is: {textbooks[book]}")
        else:
            print(f"{book} is not found in the dictionary.")
    
    elif choice == "4":
        # Print all books and their costs
        print("\nBooks and their costs:")
        for book, cost in textbooks.items():
            print(f"{book.capitalize()}: {cost}")
    
    elif choice == "5":
        # Exit the program
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")
