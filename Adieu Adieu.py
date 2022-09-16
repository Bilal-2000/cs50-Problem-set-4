def main():
    index = 0
    names = []
    check_adieu(index, names)


def check_adieu(index, names):
    while True:
        try:
            names += [input("Name: ")]
        except KeyboardInterrupt:
            if len(names) == 1:
                print()
                print(f"Adieu, adieu, to {names[index]}")
                break
            elif len(names) == 2:
                print()
                second = "".join(names[1])
                print(f"Adieu, adieu, to, {names[index]} and {second}")
                break
            elif len(names) > 2:
                print()
                rest = names[1: -1]
                rest_str = ", ".join(rest)
                last = names[-1]
                print(
                    f"Adieu, adieu, to {names[index]}, {rest_str} and {last}")
                break


main()
