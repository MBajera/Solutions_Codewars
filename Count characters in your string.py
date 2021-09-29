def count(string):
    my_dict = {}
    for dig in string:
        if dig not in list(my_dict.keys()):
            my_dict[dig]=string.count(dig)
    return my_dict