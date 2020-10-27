import math

def bisect(sorted_list, target):
    # print('list: ')
    # print(sorted_list)
    # print()
    # print('target:', target)

    length = len(sorted_list)
    middle = math.floor(length/2)

    if length == 0:
        return None
    elif sorted_list[middle] == target:
        return middle
    elif length == 1:
        return None
    elif sorted_list[middle] < target:
        result = bisect(sorted_list[ middle + 1 : ], target)
        if result == None:
            return None
        else:
            return middle + 1 + result
    else: 
        return bisect(sorted_list[ : middle ], target)