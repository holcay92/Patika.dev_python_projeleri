# h.halil olcay
def flatten( raw_list ):
    for item in raw_list:
        if type(item) == list:
            flatten(item)       # recursive function
        else:
            result.append(item)


if __name__ == '__main__':
    result = []
    raw_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
    flatten(raw_list)
    print(result)