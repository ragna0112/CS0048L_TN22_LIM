import random

print("\nNumber Guessing Game")

def menu():
    print("\nMenu:")
    print(" 1. Play Number Guessing Game")
    print(" 2. Exit")

def play_game():
    guess_num = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input(" Guess the number (1-100): ")

        if not guess.isdigit():
            print("Invalid input. Choose a number from 1-100")
            continue

        guess = int(guess)
        attempts += 1

        if guess < guess_num:
            print(" Too low!")
        elif guess > guess_num:
            print(" Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            play_game()
        elif choice == '2':
            print("Thank you for using the number guessing game")
            break
        else:
            print("Invalid choice. Choose from (1-2) pls.")

main()
