import os


def get_words_from_file(filename="test_file.txt"):
    """Reads words from a file and returns them in a list (all uppercase)."""
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        print("Current working directory:", os.getcwd())
        return []
    
    words = []
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                words.append(word.upper())
    return words

def build_frequency_dict(words):
    """Counts occurrences of each word and returns a dictionary."""
    the_dictionary = {}
    for word in words:
        # Get current count (default 0) and increment
        the_dictionary[word] = the_dictionary.get(word, 0) + 1
    return the_dictionary

def find_and_print_mode(the_dictionary):
    """Calculates the max frequency and prints the mode(s)."""
    if not the_dictionary:
        print("The dictionary is empty.")
        return

    max_count = max(the_dictionary.values())
    for word, count in the_dictionary.items():
        if count == max_count:
            print("The mode is:", word)

def main():
    # Prompt user, using 'data.txt' as a fallback if they enter nothing
    filename = input("Enter the filename: ").strip()

    # Step 1: Read
    word_list = get_words_from_file(filename)
    
    # Step 2: Count
    freq_dict = build_frequency_dict(word_list)
    
    # Step 3: Analyze
    find_and_print_mode(freq_dict)

if __name__ == "__main__":
    main()