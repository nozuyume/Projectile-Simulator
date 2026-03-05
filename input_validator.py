import math

def get_float_input(prompt, min_val = None, max_val = None, allow_zero = False):
    """
    Used in prompts to check if the
    input given is between the minimum and maximum
    values and reprompts if it isn't.
    """
    while True: 
        try: 
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be <= {max_val}")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number value.")

def get_forces():
    """
    Allows user to add as many forces
    and adds those to a list of forces,
    then allows user to exit loop.
    """
    forces = []
    while True:
        add_force = input("Add a constant force! (y/n): ").strip().lower()
        if add_force == 'n':
            break
        elif add_force == 'y':
            mag = get_float_input("Magnitude (N>0): ", min_val = 0, allow_zero = False)
            dir_deg = get_float_input("Direction (degrees, -180 to 180): ", min_val = -180, max_val = 180, allow_zero = True)
            forces.append((mag, math.radians(dir_deg)))
        else:
            print("Please enter 'y' or 'n'.")

    return forces