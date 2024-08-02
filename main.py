import sqlite3
import datetime

# Connecting to Expense database 
connection = sqlite3.connect("Expenses.db")
cursor = connection.cursor() #accessing to database

# Create the Expenses table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Expenses (
                    Date TEXT,
                    Description TEXT,
                    Category TEXT,
                    Price REAL)''')
connection.commit()

print("Welcome to Expense Tracker!\n")
print("Advantage: Keep track of the expenses of individuals\n")
print("Follow the below instructions for successful usage of Expense Tracker\n")
print("For entering new expenses enter your choice as 1\n")
print("For viewing the expense summary enter your choice as 2\n")

# Initializing while loop which will iterate until the user desires to exit from the program 
while True:
    try:
        user_choice = int(input("Enter your choice:"))
        
        if user_choice == 1:
            date = input("Enter the date of the expense (YYYY-MM-DD):")
            description = input("Enter the description of the expense:")
            
            cursor.execute("SELECT DISTINCT Category FROM Expenses")
            categories = cursor.fetchall() # Get the data under the specified column i.e. pointing to the Category column
            
            # Providing the user to select any choice based on their requirement i.e. for accessing existing category or for creating new category
            print("Select a category by number:") 
            for i, c in enumerate(categories):
                print(f"{i + 1}. {c[0]}")
            print(f"{len(categories) + 1}. Create a new category") # Initializing the condition for creating a new category
            
            category_choice = int(input())
            if category_choice == len(categories) + 1: # Validifying the condition for creating a new category
                category = input("Enter the new category name:")
            else:
                category = categories[category_choice - 1][0]
            
            price = float(input("Enter the price of the expense:"))
            
            # Insertion of values into specific columns of the Expense table
            cursor.execute("INSERT INTO Expenses (Date, Description, Category, Price) VALUES (?, ?, ?, ?)",
                           (date, description, category, price))
            connection.commit() # Saving the changes
            
        elif user_choice == 2:
            print("Select an option:")
            print("For viewing all expenses enter your choice as 1")
            print("For viewing monthly expenses by category enter your choice as 2")
            view_choice = int(input("Enter your choice:"))
            
            if view_choice == 1:
                cursor.execute("SELECT * FROM Expenses") # Select everything from the table
                expenses = cursor.fetchall()
                for expense in expenses:
                    print(expense)
                    
            elif view_choice == 2:
                month = input("Enter the month (MM):")
                year = input("Enter the year (YYYY):")
                cursor.execute("""SELECT Category, SUM(Price) FROM Expenses
                                  WHERE strftime('%m', Date) = ? AND strftime('%Y', Date) = ?
                                  GROUP BY Category""", (month, year))
                expenses = cursor.fetchall()
                for expense in expenses:
                    print(f"Category: {expense[0]}, Total: {expense[1]}")
            else:
                print("Invalid choice.")
                
        else:
            print("Invalid choice.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    repeat = input("Would you like to do something else (y/n)?\n")
    if repeat.lower() != "y":
        break

connection.close()
