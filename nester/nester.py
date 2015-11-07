"""This is the "nester.py" module for printing lists that may or may not include nested links"""
def print_lol(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level+1)
        else:
            for tab_stop in range(level):
                if indent:
                   print("\t", end='')
            print(each_item)

