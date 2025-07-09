import random

def play_game():
    number = random.randint(1, 200)
    
    while True:
        try:
            guess = int(input("Go ahead. Guess!\nGuess: "))
            if guess < number:
                print("The guess of the number that you have entered is too low")
                print("Try Again!")
            elif guess > number:
                print("The guess of the number that you have entered is too high")
                print("Try Again!")
            else:
                print("🎉 Congratulations! You guessed the number correctly!")
                break
        except ValueError:
            print("Please enter a valid number.")

    print(f"Nope. The number I was thinking of was {number}")
    return

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing! Goodbye!")
            break
name = input("Enter your name: ")
print(f"{name}, we are going to play a game.")
main()
