import pyfiglet

def validate_user_input_play_again(user_input):
    while user_input.lower().strip() not in ["y", "n"]:
        user_input = input("Wrong input. Try again: ").lower().strip()
    return user_input.lower()

def get_person_details(data_item):
    return f"{data_item.get('name')}, a {data_item.get('description')}, from {data_item.get('country')}."

def validate_user_input_compare(user_input):
    while user_input.upper().strip() not in ["A", "B"]:
        user_input = input("Wrong input. Try again: ").upper().strip()
    return user_input.upper().strip()

def print_compare(data_item1, data_item2):
    print("Compare A: " + get_person_details(data_item1))
    print(pyfiglet.figlet_format("VS"))
    print("Against B: " + get_person_details(data_item2))