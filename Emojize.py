import emoji


def main():
    str = input("Input: ")
    check_emoji(str)


def check_emoji(str):
    index = str.index(":")
    temp = str[0:index]
    string = str[index:]

    print("Output: ", temp, emoji.emojize(string, language='alias'), sep="")


main()
