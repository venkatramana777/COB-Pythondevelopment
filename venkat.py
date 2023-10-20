import string

# Function to count unique words and their occurrences in a text
def count_unique_words(text):
    word_count = {}
    
    lines = text.split('\n')
    for line in lines:
        words = line.split()
        for word in words:
            # Remove punctuation and convert to lowercase
            word = word.strip(string.punctuation).lower()
            
            if word:
                word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

# Main program
if __name__ == "__main__":
    # Replace this with your own text or sentence
    text = "HELLO THIS IS VENKATARAMANA FROM SIDDHARTH COLLEGE THIS IS MY FIRST TASK IN CODESONBYTES."

    unique_word_count = count_unique_words(text)
    
    print("Unique words and their occurrences:")
    for word, count in unique_word_count.items():
        print(f"{word}: {count}")
