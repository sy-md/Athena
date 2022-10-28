class hashmap:
    def __init__(self):
        self.size = 20
        self.ht = [[] for _ in range(0, self.size)]
    """
    hashtable:
    create a list of list/buckets

    given key is hashed by module the hashtable
    a bucket will be the ht[hashed key]

    collision:
        set a false var
        enumerate throught your key bucket
            seperate the indices
            and check for key if found
        else:
        bucket[i/num] ((_,_))
        or
        bucket.append((_,_))

    """
    def set(self,key,data):
        hashed_key = hash(key) % self.size
        buckets = self.ht[hashed_key]

        exist = False
        for i , kv in enumerate(buckets):
            k,v = kv
            if key == k:
                exist = True
                break

        if exist:
            buckets[i] = ((key,data))
        else:
            buckets.append((key,data))

    def get(self,key):

        hashed_key = hash(key) % self.size
        buckets = self.ht[hashed_key]

        found = False
        for i , kv in enumerate(buckets):
            k,v = kv
            if key == k:
                found = True
                break
        if found:
            return key
        else:
            print("not found")


h = hashmap()


h.set("big_house", "martell")
h.set("med_house", "tony")
h.set("small_house", "emma")

print(h.ht)




