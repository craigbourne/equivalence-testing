def equivalence_partition(iterable, relation):
    classes = []
    partitions = {}
    for o in iterable:  # for each object
        # find the class it is in
        found = False
        for c in classes:
            if relation(next(iter(c)), o):  # is it equivalent to this class?
                c.add(o)
                partitions[o] = c
                found = True
                break
        if not found:  # it is in a new class
            classes.append(set([o]))
            partitions[o] = classes[-1]
    return classes, partitions


def equivalence_enumeration(iterable, relation):
    classes, partitions = equivalence_partition(iterable, relation)
    ids = {}
    for i, c in enumerate(classes):
        for o in c:
            ids[o] = i
    return classes, partitions, ids


def check_equivalence_partition(classes, partitions, relation):
    for o, c in partitions.items():
        for _c in classes:
            assert (o in _c) ^ (not _c is c)
    for c1 in classes:
        for o1 in c1:
            for c2 in classes:
                for o2 in c2:
                    assert (c1 is c2) ^ (not relation(o1, o2))


def test_equivalence_partition():
    relation = lambda x, y: abs(x - y) <= 2  # Group numbers within 2 of each other
    classes, partitions = equivalence_partition(
        range(-10, 11),
        relation
    )
    check_equivalence_partition(classes, partitions, relation)
    for c in classes: print(c)
    for o, c in partitions.items(): print(o, ':', c)

def performance_test():
    import time
    relation = lambda x, y: (x - y) % 4 == 0
    start_time = time.time()
    classes, partitions = equivalence_partition(range(10000), relation)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

if __name__ == '__main__':
    test_equivalence_partition()
