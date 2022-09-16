import sys
import pyfiglet
import random


def main():
    # To get all the fonts present in pyfiglet
    fonts_list = pyfiglet.FigletFont.getFonts()
    print_word(fonts_list)


def print_word(fonts_list):

    if len(sys.argv) == 1:
        str = input("Input: ")
        # To get a random font if argv is 1
        pyfiglet.print_figlet(str, random.choice(fonts_list))

    elif len(sys.argv) == 3:
        # Setting each argv in variables
        font = sys.argv[1]
        font_style = sys.argv[2]

        if font == "-f" or font == "--font":
            if font_style in fonts_list:
                str = input("Input: ")
                pyfiglet.print_figlet(str, font_style)
            else:
                print("Invalid usage")
                sys.exit()
        else:
            print("Invalid usage")
            sys.exit()

    else:
        print("Invalid usage")
        sys.exit()


main()
