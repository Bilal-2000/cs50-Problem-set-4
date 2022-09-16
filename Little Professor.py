import random


def main():
    wrong = count = 0
    score = 1
    level = get_level()
    generate_integer(level, score, wrong, count)


def get_level():
    while True:
        try:
            integer = int(input("Level: "))
            if integer in range(1, 4):
                return integer
            else:
                continue
        except ValueError:
            continue


def generate_integer(level, s, w, c):
    continuos = 0
    while True:
        c += 1
        if c == 10:
            print(f"Score: {s}")
            break
        x = random.randint(1, 10)
        y = random.randint(1, 10)

        while True:
            try:
                ans = int(input(f"{x} + {y} = "))
            except ValueError:
                continue
            else:
                res = x + y
                if res == ans:
                    s += 1
                    break
                else:
                    print("EEE")
                    continuos += 1
                    w += 1
                    if w == 3 and continuos == 3:
                        print(f"{x} + {y} = {res}")
                        w = continuos = 0
                        break
                    else:
                        continue


main()
