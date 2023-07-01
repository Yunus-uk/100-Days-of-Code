FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ param filepath Read a text file
    return List of to do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# file = open('todos.txt', 'r')
# todos = file.readlines()  # readlines() makes into a LIST read on own DOES NOT e.g file.read() on reads
# file.close()


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the test file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# print(__name__)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())

FREEZING_POINT = 0
BOILING_POINT = 100


def water_state(temp):
    if temp < FREEZING_POINT:
        return "Solid"
    elif temp >= BOILING_POINT:
        return "Gas"
    else:
        return "Liquid"


def count(phrase):
    return phrase.count('.')


def convert(feet, inches):
    meters = (feet * 0.3048) + (inches * 0.0254)
    return meters
