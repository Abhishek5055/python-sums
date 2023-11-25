def calculate_word_frequency(word, sentences):
    word_count = 0
    for sentence in sentences:
        words = sentence.split()  # Split the sentence into words
        word_count += words.count(word)
    return word_count

# Sample 2D list of sentences
sentences_2d_list = [
    "This is a sample sentence",
    "Another sample sentence",
    "Yet another example sentence with sample"
]

# Get user input for the word to search
search_word = input("Enter the word to count: ")

# Calculate and print the frequency of the word
frequency = calculate_word_frequency(search_word, sentences_2d_list)
print(f"The word '{search_word}' appears {frequency} times in the sentences.")
