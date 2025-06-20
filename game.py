import random
def main():
    rand_nmb = random.randint(1, 100)
    print("lol")
    user_input = input(f"I`ve guessed a random number from 1 to 100. Try and guess it\n")
    guess = int(user_input)
    guessing(rand_nmb, guess)
def guessing(rand_nmb, user_guess):
        isright = False
        while isright == False:
            if rand_nmb == user_guess:
                print("You guessed right\n")
                isright = True
            elif rand_nmb > user_guess:
                print("You guessed lower")
                new_input = input("Try again")
                user_guess = int(new_input)
            else:
                print("You guessed higher")
                new_input = input("Try again")
                user_guess = int(new_input)
if __name__ == "__main__":
    main()

