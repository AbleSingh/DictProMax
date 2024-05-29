def load_words(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def filter_words_by_length(words, length):
    return [word for word in words if len(word) == length]

def is_valid_word(word, letter_counts):
    word_letter_counts = {}
    for letter in word:
        if letter in word_letter_counts:
            word_letter_counts[letter] += 1
        else:
            word_letter_counts[letter] = 1
    
    for letter, count in word_letter_counts.items():
        if letter_counts.get(letter, 0) != count:
            return False
    return True

def find_matching_words(input_word, words):
    input_word = input_word.lower()
    letter_counts = {}
    for letter in input_word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    
    candidate_words = filter_words_by_length(words, len(input_word))
    return [word for word in candidate_words if is_valid_word(word, letter_counts)]

def main():
    all_words = load_words("words_alpha.txt")
    input_word = input("Enter the letters: ").strip()
    matching_words = find_matching_words(input_word, all_words)
    
    for word in matching_words:
        print(word)
        print_word_meanings(word)

from definition import meaningGet

def print_word_meanings(word):
    print(f"{word} ::")
    meaningGet(word)
    print("")

if __name__ == "__main__":
    main()