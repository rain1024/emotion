from data import find


def response(term):
    item = find(term)
    if item:
        item.display()
        print()
    else:
        print(f"Not found \"{term}\"")

# response("buồn")
# response("vui")
# response("hạnh phúc")
# response("bất ngờ")
response("giận dữ")


# while True:
#     term = input("\n#\n")
#     response()
