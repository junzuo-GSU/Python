fileName = input("Enter the filename: ")

words = []

# Use 'with' to ensure the file is closed automatically
with open(fileName, 'r') as f:
    for line in f:
        for word in line.split():
            words.append(word.upper())

# Obtain the set of unique words and their frequencies
theDictionary = {}
for word in words:
    number = theDictionary.get(word, None)
    if number == None:
        # word entered for the first time
        theDictionary[word] = 1
    else:
        # word already exists, increment count
        theDictionary[word] = number + 1

# Determine the mode (most frequent word)
if theDictionary:
    max_count = max(theDictionary.values())
    for (word, count) in theDictionary.items():
        if count == max_count:
            print("The mode is:", word)