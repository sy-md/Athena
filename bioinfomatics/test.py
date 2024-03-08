from itertools import permutations 

num = 6

seq = [i+1 for i in range(num)]

perm = list(permutations(seq))

print(f"{len(perm)}")

for i in perm:
	print(" ".join(map(str, i))	)





