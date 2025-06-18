animals = [
    {"name": "Fluffy", "type": "dog"},
    {"name": "Parsley", "type": "dog"},
    {"name": "Ginger", "type": "cat"},
    {"name": "Biscuit", "type": "cat"},
    {"name": "Poppet", "type": "cow"},
]

def say_hello_to_pets(pets):
    try:
        for pet in pets:
            hello_message = ""

            if pet["type"] == "dog":
                hello_message = "Woof"
                pet_name  = pet["name"]
            elif pet["type"] == "cat":
                hello_message = "Meow"
                pet_name = pet["name"]
            else: 
                raise ValueError(f'Unknown pet type "{pet["type"]}"')

            print(f"{hello_message}, {pet_name}!")
    except ValueError as e:
        print(f'ERROR: {e}')
    
if __name__ == "__main__":
    say_hello_to_pets(animals)