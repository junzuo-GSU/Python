'''
Docstring for chapter_6.responsibility_drieven_example

This module demonstrates a simple text analysis application structured around
the concept of responsibility-driven design. It separates concerns into three distinct roles: 
The Librarian (data access), 
The Analyst (logic/calculations), and 
The Presenter (user interface). 
Each role has a clear responsibility, making the code easier to maintain and extend.

'''

import os

# --- ROLE: The Librarian (Data Access) ---
def load_text_from_file(file_name):
    """Responsibility: Handle the 'knowing' of file existence and reading."""
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            return f.read()
    return None

# --- ROLE: The Analyst (Logic/Calculations) ---
def get_readability_metrics(text):
    """Responsibility: Transform raw text into statistical data."""
    words = max(1, len(text.split()))
    sentences = max(1, sum(1 for char in text if char in ".?!"))
    # We return a dictionary so the 'Presenter' knows what's what
    return {"words": words, "sentences": sentences}

# --- ROLE: The Presenter (User Interface) ---
def display_results(stats):
    """Responsibility: Format data for human consumption."""
    print(f"\n--- Analysis Results ---")
    print(f"Words: {stats['words']}")
    print(f"Sentences: {stats['sentences']}")

def run_menu():
    """Responsibility: Coordinate the flow of the application."""
    current_text = ""
    while True:
        print("\n1. Load  2. Analyze  3. Exit")
        choice = input("Select: ")
        
        if choice == '1':
            name = input("Filename: ")
            current_text = load_text_from_file(name)
            if current_text: print("Loaded.")
            
        elif choice == '2':
            if current_text:
                stats = get_readability_metrics(current_text)
                display_results(stats)
            else:
                print("No text loaded.")
                
        elif choice == '3':
            break

if __name__ == "__main__":
    run_menu()