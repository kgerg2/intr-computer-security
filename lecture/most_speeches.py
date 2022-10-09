from collections import Counter; print(Counter(line[:-1] for line in open("shakespeare.txt").readlines() if line.isupper()).most_common()[0][0])

# with open("lecture/shakespeare.txt") as f:
    # print(Counter(line for line in f.read().splitlines() if line.isupper()).most_common()[0][0])

# print(Counter(line for line in open("shakespeare.txt").read().splitlines() if line.isupper()).most_common()[0][0])