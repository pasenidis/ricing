from datetime import datetime
from json import loads
from random import choice
from shutil import disk_usage


def main():
    """Main function that returns the values to the shell script that runs this."""
    time = datetime.now()
    time = time.strftime("%m/%d/%Y, %H:%M:%S")
    print(f"{check_session()} / {get_disk_usage()} / {get_virtual_memory()} / {time}")


def get_quote():
    """Loads a quote object that contains a 'text' and a 'author' keys"""
    data = loads(open('quotes.json').read())
    selected = choice(data)
    text = selected['text']
    author = selected['author']
    return f'{text[:30]}.. — {author}'


def get_disk_usage():
    total, used, free = disk_usage("/")
    del total, used
    return f'💾 {free // (2**30)} GB'


def get_virtual_memory():
    try:
        from psutil import virtual_memory
        ram_usage = virtual_memory().percent
        return f'{ram_usage}%'
    except ImportError:
        return 'psutil is not installed'


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
