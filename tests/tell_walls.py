def hex_to_walls(hex_value):
    directions = ["North", "East", "South", "West"]

    try:
        # convert hex string to integer
        value = int(hex_value, 16)
    except ValueError:
        print("Invalid hex value")
        return

    walls_up = []

    # check each of the 4 bits
    for i in range(4):
        if value & (1 << i):
            walls_up.append(directions[i])

    if walls_up:
        print("Walls up:", ", ".join(walls_up))
    else:
        print("No walls are up")


# Example usage
user_input = input("Enter hex value (e.g. A, 3, F): ")
hex_to_walls(user_input)