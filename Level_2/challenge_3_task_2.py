people = [
    {
        "name": {"first": "Jane", "last": "Doe"},
        "age": 42,
        "employed": True
    },
    {
        "name": {"first": "Tom", "last": "Smith"},
        "age": 18,
        "employed": True
    },
    {
        "name": {"first": "Mariam", "last": "Coulter"},
        "age": 66,
        "employed": False
    },
    {
        "name": {"first": "Gregory", "last": "Tims"},
        "age": 8,
        "employed": False
    }
]

def list_details_all(people):
    for person in people:
        name = f"{person['name']['first']} {person['name']['last']}"
        age = person['age']
        employed = "Employed" if person['employed'] else "Unemployed"

        print(f"Name: {name} \nAge: {age} \nStatus: {employed}")

def list_details_name(people):
    names = [f"{person['name']['first']} {person['name']['last']}".strip() for person in people]

    for name in names:
        print(f'{name}')

def add_person():
    person = {}

    full_name = input("Enter full name (first and last): ").strip().split()
    age = input("Enter age: ").strip()
    employed = input("Is the person employed? (yes/no): ").strip().lower()

    first = full_name[0]
    last = " ".join(full_name[1:]) if len(full_name) > 1 else ""

    person = {
        "name": {"first": first, "last": last},
        "age": int(age),
        "employed": employed == 'yes' or employed == 'y'
    }

    people.append(person)
    list_details_all(people)

def remove_person():
    list_details_name(people)

    name_input = input("Enter the full name or first name of the person to remove: ").strip().lower()
    to_remove = []

    for person in people:
        first = person["name"]["first"].lower()
        last = person["name"]["last"].lower()
        full = f"{first} {last}".strip()

        if name_input == first or name_input == full:
            to_remove.append(person)

    if not to_remove:
        print("No matching person found.")
        remove_person()
    else:
        for person in to_remove:
            people.remove(person)
        print(f"Removed {len(to_remove)} person.")
        list_details_all(people)

def user_prompt():
    choice  = input("Would you like to 'Add', 'Remove' or 'List' a person from the list? ").strip().lower()

    if choice == 'add' or choice == 'a':
        add_person()
    elif choice == 'remove' or choice == 'r':
        remove_person()
    elif choice == 'list' or choice == 'l':
        list_details_all(people)
    else:
        print("Invalid choice. Please enter 'Add' or 'Remove'. ")
        user_prompt()

while True:
    user_prompt()