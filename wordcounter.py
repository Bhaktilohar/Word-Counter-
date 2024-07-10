def count_words(text):
    words = text.split()
    return len(words)

user_input = input("Enter some text: ")
word_count = count_words(user_input)

print(f"The number of words in the text is: {word_count}")
