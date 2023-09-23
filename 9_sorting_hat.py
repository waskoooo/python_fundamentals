while True:
    name = input()

    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    if name == "Voldemort":
        print("You must not speak of that name!")
        break

    name_length = len(name)

    if name_length < 5:
        house = "Gryffindor"
    elif name_length == 5:
        house = "Slytherin"
    elif name_length == 6:
        house = "Ravenclaw"
    else:
        house = "Hufflepuff"

    print(f"{name} goes to {house}.")