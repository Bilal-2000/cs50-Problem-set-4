import requests
import sys
import json


def main():
    val = Argument_check()
    try:
        val = float(val)
    except ValueError:
        print("Can't be converted to float")
        sys.exit()
    else:
        try:
            res = requests.get(
                'https://api.coindesk.com/v1/bpi/currentprice.json').json()
        except requests.RequestException:
            print("File Request Error RE-RUN!!")
            sys.exit()
        else:
            rate = res.get("bpi").get("USD").get("rate_float")
            total = val * rate
            print(f"${total:,.4f}")


def Argument_check():
    if len(sys.argv) == 1:
        print("Missing command line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit()

    try:
        system = int(sys.argv[1])
    except ValueError:
        print("Not a number")
        sys.exit()
    else:
        val = sys.argv[1]
        return val


main()
