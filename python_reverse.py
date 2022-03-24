#h.halil olcay
# input: [[1, 2], [3, 4], [5, 6, 7]]
# output: [[[7, 6, 5], [4, 3], [2, 1]]

raw_input = [[1, 2], [3, 4], [5, 6, 7]]
print(raw_input)
raw_input.reverse()

for sub in raw_input:
    sub.reverse()
print(raw_input)