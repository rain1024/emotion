from data import find


def response(term):
    item = find(term)
    if item:
        item.display()
        print()
    else:
        print(f"Not found \"{term}\"")


if __name__ == '__main__':
    while True:
        term = input("\n#\n")
        response(term)
