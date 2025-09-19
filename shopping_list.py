
shopping_list = ["apples", "bread", "milk", "cheese"]
item_found = False

while not item_found:
    item = input("search for an item in your list (or 'q' to quit): ")
    if item.lower() == "q":
        break # exit the loop if user enter q
    if item in shopping_list:
        item_found = True
        print(f"{item} is your shopping list. ")
    else:
        print(f"{item} is not on your list. ")