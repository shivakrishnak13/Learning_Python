import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == "yes"

def main():
    user_score = 0
    computer_score = 0
    draws = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "draw":
            print("It's a draw!")
            draws += 1
        elif result == "user":
            print("Congratulations! You won!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}, Draws: {draws}")

        if not play_again():
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
