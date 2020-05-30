from data import find

while True:
    term = input("\n#\n")
    item = find(term)
    if item:
        print(item.display(), end="\n")
    else:
        print(f"Not found \"{term}\"")