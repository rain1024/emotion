from data import Emotions


def response(term):
    item = Emotions.find(term)
    if item:
        item.display()
        print()
    else:
        print(f"Không tìm thấy \"{term}\"")


if __name__ == '__main__':
    while True:
        term = input("\n#\n")
        response(term)
