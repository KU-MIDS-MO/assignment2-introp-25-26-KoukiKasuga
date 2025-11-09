def swap_ends(L, k):
    new_list = L[:]
    if k <= 0 or k > len(L)/2:
        return (new_list, 0)
    
    print(type(new_list))
    num_swaps = 0

    for i in range(k):
        new_list.append(new_list[i])
        new_list.pop(i)
        new_list.insert(0, new_list[-i -2])
        new_list.pop(-i-2)
        num_swaps += 1

    return new_list, num_swaps

    pass