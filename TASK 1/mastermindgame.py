#MASTER MIND GAME
import random

def get_digits(number):
    """Convert the number to a list of its digits."""
    return [int(digit) for digit in str(number)]

def generate_hint(secret, guess):
    """Generate a hint showing which digits are correct."""
    secret_digits = get_digits(secret)
    guess_digits = get_digits(guess)
    
    correct_digits = ['-' if g != s else s for s, g in zip(secret_digits, guess_digits)]
    return ''.join(map(str, correct_digits))

def play_game():
    """Main function to play the game."""
    attempts = {}
    print("Player 1, set your number:")
    secret_number = int(input("Enter a multi-digit number: "))
    print("\n" * 50)
    attempts_player2 = 0
    while True:
        guess = int(input("Player 2, guess the number: "))
        attempts_player2 += 1
        if guess == secret_number:
            print(f"Correct! Player 2 guessed the number in {attempts_player2} attempts.")
            break
        else:
            hint = generate_hint(secret_number, guess)
            print(f"Hint: {hint}")
    
    attempts['Player 2'] = attempts_player2
    print("Now it's Player 2's turn to set the number.")
    secret_number = int(input("Player 2, enter a multi-digit number: "))
    print("\n" * 50)  
    attempts_player1 = 0
    while True:
        guess = int(input("Player 1, guess the number: "))
        attempts_player1 += 1
        if guess == secret_number:
            print(f"Correct! Player 1 guessed the number in {attempts_player1} attempts.")
            break
        else:
            hint = generate_hint(secret_number, guess)
            print(f"Hint: {hint}")
    
    attempts['Player 1'] = attempts_player1
    if attempts['Player 1'] < attempts['Player 2']:
        print("Player 1 wins and is crowned Mastermind!")
    else:
        print("Player 2 wins and is crowned Mastermind!")
    
if __name__ == "__main__":
    play_game()