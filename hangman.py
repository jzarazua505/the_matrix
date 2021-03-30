from random import choice

PUNCT = {" ", "'", "!", "?"}

def show_board(phrase, guesses):
    for c in phrase:
        if c.lower() in guesses or c in PUNCT:
            print(c, end=" ")
        else:
            print("_", end=" ")
    print()

def show_mistakes(phrase, guesses):
    print("Wrong answers:", end=" ")
    for c in guesses:
        if c not in phrase.lower():
            print(c, end=" ")
    print()
         
def get_guess(guesses):
    valid = False
    while not valid:
        # ask player for guess
        players_guess = input("What letter are you guessing? ")[0:1].lower()
        if not players_guess.isalpha():
            print("That is not a letter. Guess again")
        elif players_guess in guesses:
            print("You already guessed that letter. Guess again.")
        else:
            valid = True
    return players_guess

def win(phrase, guesses):
    for c in phrase:
        if c.lower() not in guesses and c not in PUNCT:
            return False
    return True

if __name__ == "__main__":
    # setup
    with open("kanye_songs.txt") as s:
        phrases = s.read().splitlines()

    phrase = choice(phrases)
    guesses = set()
    mistakes = 0
    max_mistakes = 6
    while mistakes != max_mistakes and not win(phrase, guesses):
        show_board(phrase, guesses)
        # shows the players mistakes
        show_mistakes(phrase, guesses)
        # show the player the number of wwrong guesses they have left
        print(f"Chances left: {max_mistakes - mistakes}")
        # returns the players guess
        players_guess = get_guess(guesses)
        # check if guess is wrong
        if players_guess not in phrase:
            mistakes += 1
        guesses.add(players_guess)
    if mistakes == max_mistakes:
        print(f"You lose. The phrase was '{phrase}'.")
    else:
        show_board(phrase, guesses)
        print("You win")
