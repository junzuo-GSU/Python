import os

# --- 1. Sub-functions for specific tasks ---

def get_file_content():
    """Option 1: Handles user input for filename and returns content."""
    file_name = input("Enter the filename to load: ")
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            content = f.read()
            print(f"\n--- Success: '{file_name}' loaded! ---")
            return content
    else:
        print("\n--- Error: File not found. ---")
        return ""

def show_basic_stats(text):
    """Option 2: Displays word and sentence counts."""
    if not text:
        print("! Please load a file first (Option 1).")
        return
    
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')
    print(f"\nAnalysis: {max(1, words)} words and {max(1, sentences)} sentences found.")

def show_full_report(text):
    """Option 3: Placeholder for your Flesch Index logic."""
    if not text:
        print("! Please load a file first (Option 1).")
        return
    
    # You would call your compute_flesch_index functions here
    print("\nFull Report: Detailed readability metrics would appear here.")

def display_menu():
    """Helper to show the UI."""
    print("\n" + "="*25)
    print("   TEXT ANALYSIS MENU")
    print("="*25)
    print("1. Load a Text File")
    print("2. Count Words and Sentences")
    print("3. View Full Readability Report")
    print("4. Exit")
    print("="*25)

# --- 2. The Simple Mainline Logic ---

def main():
    """The 'Manager' function that controls the flow."""
    current_text = ""
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            current_text = get_file_content()
        elif choice == '2':
            show_basic_stats(current_text)
        elif choice == '3':
            show_full_report(current_text)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()