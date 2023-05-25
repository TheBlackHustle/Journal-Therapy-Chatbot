**
 * [Journal Therapy Chatbot]
 * [This project implements a journal therapy chatbot powered by artificial intelligence (AI). 
 *The chatbot utilizes the Chroma vector database for analyzing and processing journal entries to provide 
 *feedback and advice based on user queries.]
 *
 * Copyright [2023] [Devin Jackson]
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */




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
