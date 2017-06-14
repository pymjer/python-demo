import collections
with open('./puzzle3.txt', 'r') as f:
    puzzle = f.read()
    od = collections.OrderedDict()
    for c in puzzle:
        od[c] = od.get(c, 0) + 1

    avg = len(puzzle) / len(od)
    result = ''.join([an for an in od if od[an] < avg])
    print(result)
