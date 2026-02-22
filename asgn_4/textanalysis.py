"""
Program: textanalysis.py

Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file.
The calcualtion includes: number of lines and number of words and number of syllables in the text file.
The syllable counting is done by counting the number of vowel groups in each word, 
with adjustments for silent 'e', 'es', and 'ed' endings, and treating 'le' endings as single syllables. 
This approach provides a more accurate syllable count for English words, 
which is essential for calculating the Flesch Index and Grade Level Equivalent correctly.
as single syllables.
"""

# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

# Count the words
words = len(text.split())

# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    vowelSeen = False        # Corrects for multi-vowel syllables
    for character in word:
        if not vowelSeen and character in vowels:
            syllables += 1
            vowelSeen = True
        elif not character in vowels:
            vowelSeen = False
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")     


