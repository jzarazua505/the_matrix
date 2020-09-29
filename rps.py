from random import randint

def get_result(choice, cpu_choice):
    # Check if there was a draw
    if choice == cpu_choice:
        # Ignore all other cases if draw
        return None

    # Only check if you lost
    if choice == 1 and cpu_choice == 2:
        return False
    elif choice == 2 and cpu_choice == 3:
        return False
    elif choice == 3 and cpu_choice == 1:
        return False

    # If you didn't lose, you can assume you won
    return True

ans = "y"
score = cpu_score = 0
while ans == "y":
    choice = int(input("rock, paper, or scissors (1, 2, 3)? "))
    cpu_choice = randint(1, 3)
    print(f"CPU chose: {cpu_choice}")
    result = get_result(choice, cpu_choice)

    if result is None:
        print("draw")
    elif result:
        print("u win")
        score += 1
    else:
        print("git gud kid")
        cpu_score += 1
    
    print(f"Your score: {score}")
    print(f"CPU score: {cpu_score}")
    ans = input("would you like to play again (y/n)? ")

