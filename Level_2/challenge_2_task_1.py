import random

def generate_number():
    return random.randint(1, 100)

def get_user_input():
    try:
        user_input = input("Please enter a number: ")
        number = int(user_input)
        
        return number
    except ValueError:
        print("That's not a valid number. Please try again.")
        return get_user_input()
    
def check_user_guess(random_num, user_num):
    result = ""
    if random_num < user_num:
        result = "higher"
    elif random_num > user_num:
        result = "lower"
    else:
        result = "correct"

    return result

def guess_loop(random_num):
    attempts = []

    while True:
        user_num = get_user_input()
        
        if not attempts or user_num != attempts[-1]:
            attempts.append(user_num)

        result = check_user_guess(random_num, user_num)

        if result == "correct":
            print(f"You Won! You guessed the number {random_num} in {len(attempts)} attempts.")
            break
        elif result == "lower":
            print("Your guess is too low. Try again.")
        elif result == "higher":
            print("Your guess is too high. Try again.")
    
def check_play_again():
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()

    if play_again == 'yes' or play_again == 'y':
        return True
    elif play_again == 'no' or play_again == 'n':
        print("Thank you for playing!")
        return False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return check_play_again()

while True:
    random_num = generate_number()

    guess_loop(random_num)

    if check_play_again() == False:
        exit()