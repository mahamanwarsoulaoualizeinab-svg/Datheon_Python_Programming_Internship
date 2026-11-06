import random

HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
           |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
      =======
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
      =======
    """
]


def load_words(filename="Words.txt"):
    """Load words from the text file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            words = [
                word.strip().lower()
                for word in file.readlines()
                if word.strip().isalpha()
            ]

        if not words:
            raise ValueError("The word list is empty.")

        return words

    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        print("Make sure Words.txt is in the same folder as hangman.py.")
        return []


def display_game(secret_word, guessed_letters, attempts_left):
    """Display the current game state."""
    mistakes = 6 - attempts_left

    print("\n" + "=" * 40)
    print("          WELCOME TO HANGMAN!")
    print("=" * 40)

    print(HANGMAN_STAGES[mistakes])

    masked_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print(f"\nWord: {masked_word}")
    print(f"Attempts left: {attempts_left}")

    if guessed_letters:
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))
    else:
        print("Guessed letters: None")

    print("=" * 40)


def play_game(words):
    """Run one round of Hangman."""
    secret_word = random.choice(words)

    guessed_letters = set()
    attempts_left = 6

    while attempts_left > 0:
        display_game(secret_word, guessed_letters, attempts_left)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            return

        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess! The letter is in the word.")
        else:
            attempts_left -= 1
            print("Wrong guess! You lost one attempt.")

    display_game(secret_word, guessed_letters, attempts_left)
    print(f"\nGame over! The secret word was: {secret_word}")


def main():
    """Start the Hangman game."""
    words = load_words()

    if not words:
        return

    print("\nWelcome to the Hangman Game!")

    while True:
        play_game(words)

        play_again = input("\nWould you like to play again? (yes/no): ")
        if play_again.strip().lower() not in ("yes", "y"):
            print("\nThank you for playing Hangman!")
            break


if __name__ == "__main__":
    main()