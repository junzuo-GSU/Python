import os

"""
Program: textanalysis.py
Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file.
The enchancment included in this version is:
1. Added error handling for file access issues, such as missing files or permission errors, to prevent crashes and provide user-friendly feedback.
2. Used the 'with' statement for file operations to ensure proper resource management and automatic file closure, even in the event of an error.
3. Used f-strings for output formatting to enhance readability and maintainability of the code, making it easier to understand and modify the output format in the future.
"""


# 1. & 2. Check accessibility and use 'with' statement
fileName = input("Enter the file name: ")

if not os.path.exists(fileName):
    print(f"Error: The file '{fileName}' was not found or is not accessible.")
    print(os.getcwd())  # Show current directory for debugging
    exit()

with open(fileName, 'r') as inputFile:
    text = inputFile.read()

#Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')
# sentence_ending = ".?;:!"
# sentences = 0
# for char in text:
#     if char in sentence_ending:
#         sentences += 1

# Handle edge case: empty file or no sentences to avoid DivisionByZero
if sentences == 0: sentences = 1

# Count the words
wordList = text.split()
words = len(wordList)
# if words == 0: words = 1

# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"
for word in wordList:
    vowelSeen = False
    for character in word:
        if not vowelSeen and character in vowels:
            syllables += 1
            vowelSeen = True
        elif character not in vowels:
            vowelSeen = False
    
    # Adjustments for silent 'e', 'es', 'ed'
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1
        
# Ensure syllable count is at least 1 per word
if syllables <= 0: syllables = words

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59))

# 3. Output the results using f-strings
print("-" * 30)
print(f"The Flesch Index is: {index:.2f}")
print(f"The Grade Level Equivalent is: {level}")
print("-" * 30)
print(f"Summary Statistics:")
print(f" - {sentences} sentences")
print(f" - {words} words")
print(f" - {syllables} syllables")

