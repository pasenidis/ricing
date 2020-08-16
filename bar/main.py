from datetime import datetime
from json import loads
from random import choice


def main():
    """Main function that returns the values to the shell script that runs this."""
    time = datetime.now()
    time = time.strftime("%m/%d/%Y, %H:%M:%S")
    print(f"{check_session()} / {time}")


def get_quote():
    """Loads a quote object that contains a 'text' and a 'author' keys"""
    data = loads(open('quotes.json').read())
    selected = choice(data)
    text = selected['text']
    author = selected['author']
    return f'{text[:30]}.. — {author}'


def check_session():
    """Checks if the second is the first of a minute so it only parses a quote once."""
    if datetime.now().second == 1:
        quote = get_quote()
        with open('session.txt', 'w') as f:
            f.write(quote)
        return quote
    else:
        with open('session.txt', 'r') as f:
            x = f.read()
        return x


if __name__ == "__main__":
    main()
