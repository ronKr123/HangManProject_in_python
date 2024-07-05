def get_word_from_index(index):
    with open('wordsFile.txt', 'r') as file:
        words = file.read().strip().split(',')
        adjusted_index = (index - 1) % len(words)
        return words[adjusted_index]

def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    displayed_word = []

    for letter in secret_word:
        if letter in old_letters_guessed:
            displayed_word.append(letter)
        else:
            displayed_word.append('_')

    return ' '.join(displayed_word)

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        return False

def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) != 1:
        print("Error: Entered string contains more than one character.")
        return False

    if not letter_guessed.isalpha():
        print("Error: Entered character is not a valid English letter.")
        return False

    if letter_guessed.lower() in old_letters_guessed:
        print("Error: You have already guessed this letter.")
        return False

    return True

def print_welcome_text():
    ascii_art = r"""
        _    _
       | |  | |
       | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
       |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
       | |  | | (_| | | | | (_| | | | | | | (_| | | | |
       |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |
                            |___/
    """

    print(ascii_art)

HANGMAN_PHOTOS = {
    0: """
    x-------x
    """,
    1: """
    x-------x
    |
    |
    |
    |
    |
    """,
    2: """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    3: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    4: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
}

def print_hangman(num_of_tries):
    if num_of_tries in HANGMAN_PHOTOS:
        print(HANGMAN_PHOTOS[num_of_tries])
    else:
        print("Invalid number of tries")

def main():
    print_welcome_text()
    num = int(input("Enter an index to retrieve the word: "))
    word = get_word_from_index(num)
    if word:
        print("The Game is Started!")
        play(word, MAX_TRIES)
    else:
        print(f"Index {num} is out of range.")

def play(secret_word, max_tries):
    old_letters_guessed = []
    num_of_tries = 0

    while num_of_tries < max_tries:
        print(f"Number of tries left: {max_tries - num_of_tries}")
        print(show_hidden_word(secret_word, old_letters_guessed))
        guess_letter = input("Guess a letter: ").lower()

        if try_update_letter_guessed(guess_letter, old_letters_guessed):
            if guess_letter not in secret_word:
                num_of_tries += 1
                print_hangman(num_of_tries)
            if check_win(secret_word, old_letters_guessed):
                print("You win! The word is:", secret_word)
                return
        else:
            print("Invalid input. Try again.")
            print_hangman(num_of_tries)

    print("Game Over! The word was:", secret_word)

MAX_TRIES = 6

if __name__ == "__main__":
    main()
