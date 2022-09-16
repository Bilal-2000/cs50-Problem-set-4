import random


def main():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if level < 1:
                continue
        while True:
            try:
                guess = int(input("Guess: "))
            except ValueError:
                continue
            else:
                if guess < 1:
                    continue
                else:
                    num = random.randint(1, level)
                    if guess < num:
                        print("Too small!")
                        continue
                    elif guess > num:
                        print("Too large!")
                        continue
                    else:
                        print("Just right!")
                        return


main()
