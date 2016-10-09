# creating a function data_type using the def as used in python. hence def data_type(my_arg):
def data_type(my_arg):
    # used my_arg since it closely associates with the word "my argument"
    if type(my_arg) is str:
        return len(my_arg)

    elif my_arg is None:
        return 'no value'

    elif type(my_arg) is bool:
        if my_arg is True:
            return True
        return False

    elif type(my_arg) is int:
        if my_arg < 100:
            return 'less than 100'
        elif my_arg == 100:
            return 'equal to 100'
        else:
            return 'more than 100'

    elif type(my_arg) is list:
        if len(my_arg) >= 3:
            return my_arg[2]
        else:
            return None
    # the spaces help in the structuring of the code and grouping the code under the python programming principals and they
    # also keep the code organised.
    """below are the keywords to make the code easier to read.
    so str is the string data_type, bool is the boolean datatype, int is the integer data type and list definately for the
    lists
    """