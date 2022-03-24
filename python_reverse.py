#h.halil olcay
# input: [[1, 2], [3, 4], [5, 6, 7]]
# output: [[[7, 6, 5], [4, 3], [2, 1]]


def reverse_recursive(raw_list):
    raw_list.reverse()

    for sub in raw_list:
        if type(sub) == list:
            reverse_recursive(sub)
            #
        else: result.append(sub)

if __name__ == '__main__':
    raw_input = [[1, 2, [8, 0, 9]], [3, 4], [5, 6, 7]]
    result = []
    reverse_recursive(raw_input)
    print(raw_input)