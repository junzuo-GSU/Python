
"""
Program: textanalysis.py
Computes and displays the Flesch Index and the Grade Level Equivalent for the readability of a text file.

This program is to convert the script into a structured design with functions.

main() will be the main function that calls other functions to perform specific tasks.
load_file() will handle file loading and error handling.
count_sentences(), count_words(), and count_syllables() will perform their respective counting tasks.
count_syllables_in_word() will count syllables in a single word, including adjustments for silent 'e', 'es', 'ed', and 'le' endings.
compute_flesch_index() will calculate the Flesch Index.
compute_grade_level() will calculate the Grade Level Equivalent.
display_results() will handle the output formatting and display of results.
"""

import os

def load_file(file_name):
    """Checks for file existence and returns the content if found."""
    if not os.path.exists(file_name):
        print(f"Error: The file '{file_name}' was not found.")
        return None
   
    with open(file_name, 'r') as file:
        return file.read()

def count_sentences(text):
    """Counts sentences based on ending punctuation."""
    count = 0
    for char in text:
        if char in ".?;:!":
            count += 1
    # Returns 1 if no punctuation is found to avoid division by zero
    return max(1, count)

def count_words(text):
    """Splits text and returns the word count."""
    words = text.split()
    return max(1, len(words))

def count_syllables_in_word(word):
    """Calculates syllables in a single word with linguistic adjustments."""
    vowels = "aeiouAEIOU"
    syllables = 0
    vowel_seen = False
    
    # Clean the word of common punctuation for better suffix matching
    word = word.strip(".,!?;:").lower()
    
    for char in word:
        if char in vowels:
            if not vowel_seen:
                syllables += 1
                vowel_seen = True
        else:
            vowel_seen = False
            
    # Adjustments for silent endings
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1
        
    return max(1, syllables)

def count_syllables(text):
    """Sums syllables for all words in the text."""
    word_list = text.split()
    total = 0
    for word in word_list:
        total += count_syllables_in_word(word)
    return total

def compute_flesch_index(words, sentences, syllables):
    """Calculates the Flesch Reading Ease score."""
    return 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)

def compute_grade_level(words, sentences, syllables):
    """Calculates the Flesch-Kincaid Grade Level."""
    return int(round(0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59))

def display_results(index, level, sentences, words, syllables):
    """Formats and prints the analysis results."""
    print("-" * 30)
    print(f"The Flesch Index is: {index:.2f}")
    print(f"The Grade Level Equivalent is: {level}")
    print("-" * 30)
    print("Summary Statistics:")
    print(f" - {sentences} sentences")
    print(f" - {words} words")
    print(f" - {syllables} syllables")

def main():
    """Main execution logic."""
    file_name = input("Enter the file name: ")
    text = load_file(file_name)
    
    if text is not None:
        s_count = count_sentences(text)
        w_count = count_words(text)
        syll_count = count_syllables(text)
        
        index = compute_flesch_index(w_count, s_count, syll_count)
        grade = compute_grade_level(w_count, s_count, syll_count)
        
        display_results(index, grade, s_count, w_count, syll_count)

if __name__ == "__main__":
    main()

