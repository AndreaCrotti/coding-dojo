SIZE = 8

dic = {(0, 0, 0): 0,
       (0, 0, 1): 0,
       (0, 1, 0): 0,
       (0, 1, 1): 1,
       (1, 0, 0): 1,
       (1, 0, 1): 0,
       (1, 1, 0): 0,
       (1, 1, 1): 0,
       }


def future(current):
    assert len(current) == 3, "must pass length 3 list"
    return dic[tuple(current)]


def next(current):
    # def around(idx):
    #     return (idx-1, idx, (idx+1) % len(current))

    assert all(x == 0 or x == 1 for x in current)

    # next_idx = lambda idx: (idx + 1) % len(current)
    
    res = []
    for idx in range(len(current)):
        triple = []
        triple.append(current[idx-1])
        triple.append(current[idx])
        triple.append(current[(idx+1) % len(current)])
        res.append(future(triple))

    return res
