# Square each value in a given list, returning that same list with changed values.

def squared_values(list):
    squared_list = []
    for i in range (0,len(list)):
        value = list[i] * list[i]
        squared_list.append(value)
    return squared_list

print(squared_values([2,3,4]))
