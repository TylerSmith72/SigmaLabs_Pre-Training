def sum_num(n):
    sum = 0

    for i in range(1, n + 1):
        # if check_num_3_5(i):
        #     sum += i
        sum += i

    return sum

def product_num(n):
    product = 1

    for i in range(1, n + 1):
        # if check_num_3_5(i):
        #     product *= i
        product *= i

    return product

def check_num_3_5(n):
    # Check if the number is divisible by 3 or 5
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False

def check_num_type(n):
    try:
        num = int(n)
        
        if num < 0:
            raise ValueError()
        else:
            return True
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return False

def get_mode():
    print("1. Sum of numbers from 1 to n")
    print("2. Product of numbers from 1 to n\n")

    choice = ask_user_for_number()

    return choice

def check_mode(choice):

    if choice not in [1, 2]:
        print("Invalid choice. Please enter 1 or 2.\n")
        return False
    else:
        print(f"Mode chosen: {choice}\n")
        return True

def play_mode(choice, n):
    if choice == 1:
        result = sum_num(n)
        print(f"The sum of numbers from 1 to {n} is: {result}\n")
        exit()
    elif choice == 2:
        result = product_num(n)
        print(f"The product of numbers from 1 to {n} is: {result}\n")
        exit()

def ask_user_for_number():
    n = input("Enter a positive integer n: ")

    if not check_num_type(n):
        return ask_user_for_number()

    return int(n)

while True:
    choice = get_mode()

    # Loop until a valid choice is made
    if not check_mode(choice):
        continue

    n = ask_user_for_number()

    play_mode(choice, n)