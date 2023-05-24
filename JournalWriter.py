import os
from datetime import date

# Function to take user input and save it as a journal entry
def write_journal_entry():
    # Ask the user for their journal entry
    entry = input("What's on your mind today? ")

    # Get the current date
    today = date.today()
    # Format the date as YYYY-MM-DD
    formatted_date = today.strftime("%Y-%m-%d")

    # Use the date to create a filename
    filename = f"{formatted_date}.txt"
    
    # Specify the folder path
    folder_path = "/Users/devinjackson/Documents/PycharmProjects/Journal Project/Entries/"
    # Make sure the directory exists
    os.makedirs(folder_path, exist_ok=True)

    # Create the full file path
    file_path = os.path.join(folder_path, filename)

    # Open the file in write mode and write the entry
    with open(file_path, 'w') as file:
        file.write(entry)

    print(f"Your entry has been saved as {filename}.")

# Call the function to make a new journal entry
write_journal_entry()
