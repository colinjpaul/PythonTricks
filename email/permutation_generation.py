import itertools

count = 0

for p in itertools.permutations('123456789'):
    count += 1
    print(p)

print("total permutations: ", count)

