import random
import string

WORDS = ["python", "laptop", "coding", "intern", "github", "developer", "keyboard", "variable"]

MAX_LIVES = 6
HEART_FULL = "♥"
HEART_EMPTY = "♡"

def render_hearts(remaining, total):
    return HEART_FULL * remaining + HEART_EMPTY * (total - remaining)

def print_header():
    print("=" * 46)
    print("🕹️  Hangman — Guess the Word!".center(46))
    print("=" * 46)

def print_state(display_word, lives_left, wrong_letters, guessed_letters):
    print("\n" + "-" * 46)
    print(f"Word:   {' '.join(display_word)}")
    print(f"Lives:  {render_hearts(lives_left, MAX_LIVES)}  ({lives_left}/{MAX_LIVES})")
    if wrong_letters:
        print(f"Wrong:  {', '.join(sorted(wrong_letters))}")
    if guessed_letters:
        print(f"Tried:  {', '.join(sorted(guessed_letters))}")
    print("-" * 46)

def get_guess(guessed_letters):
    while True:
        raw = input("Enter a letter (a-z): ").strip().lower()
        if len(raw) != 1 or raw not in string.ascii_lowercase:
            print("Please enter exactly one letter (a-z).")
            continue
        if raw in guessed_letters:
            print("You already tried that letter. Pick another.")
            continue
        return raw

def play_round(word):
    display_word = ["_"] * len(word)
    guessed_letters = set()
    wrong_letters = set()
    lives_left = MAX_LIVES

    print_header()

    while lives_left > 0 and "_" in display_word:
        print_state(display_word, lives_left, wrong_letters, guessed_letters)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            for i, ch in enumerate(word):
                if ch == guess:
                    display_word[i] = guess
            print("✅ Nice! That letter is in the word.")
        else:
            lives_left -= 1
            wrong_letters.add(guess)
            print(f"❌ Nope. '{guess}' isn't in the word.")

    print_state(display_word, lives_left, wrong_letters, guessed_letters)

    if "_" not in display_word:
        print(f"\n🎉 Congratulations! You guessed the word: {word}")
    else:
        print(f"\n💀 Game Over! The word was: {word}")

def main():
    print_header()
    while True:
        word = random.choice(WORDS)
        play_round(word)
        # Ask to play again
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nThanks for playing! Goodbye 👋")
            break
        print("\n" + "=" * 46)

if __name__ == "__main__":
    main()
