# Task - 1: Input Text
def input_text():
    return input("Enter a paragraph of text: ")

# Task - 2: Word Tokenization
def word_tokenization(text):
    return text.split()

# Task - 3: Word Frequency Calculation
def word_frequency_calculation(words):
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict

# Task - 4: Display Word Frequencies
def display_word_frequencies(frequency_dict):
    sorted_freq = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    for word, freq in sorted_freq:
        print(f"{word}: {freq}")

# Task - 5: Top N Words
def top_n_words(frequency_dict, n):
    sorted_freq = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(min(n, len(sorted_freq))):
        word, freq = sorted_freq[i]
        print(f"{word}: {freq}")

# Task - 6: Word Search
def word_search(frequency_dict):
    search_word = input("Enter a word to search: ")
    if search_word in frequency_dict:
        print(f"Frequency of '{search_word}': {frequency_dict[search_word]}")
    else:
        print(f"'{search_word}' not found in the text.")

# Task - 7: Advanced Analysis (Optional)
# (Advanced analysis tasks can be added here)

text_input = input_text()
word_list = word_tokenization(text_input)
word_freq_dict = word_frequency_calculation(word_list)

print("\nWord Frequencies:")
display_word_frequencies(word_freq_dict)

n_value = int(input("\nEnter the value of N for top N words: "))
print(f"\nTop {n_value} Words:")
top_n_words(word_freq_dict, n_value)

word_search(word_freq_dict)
