#lst = [10,11,12,13,14,15,16,17,18,19]
lst = [10,20,30,40,50,18]

for i, n in enumerate(lst):
    if n >= 10:
       lst[i] = (n - 10)
       print(lst)

print("orginal",lst)
