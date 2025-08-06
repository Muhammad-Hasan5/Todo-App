FILEPATH = 'todos.txt'


def get_todos(filepath = FILEPATH):
    """
    Read a text file and return to-dos items list
    :param filepath:
    :return: to-dos list
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath = FILEPATH):
    """
    Write the to-dos items list in the text file
    :param todos_arg:
    :param filepath:
    :return: none
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)