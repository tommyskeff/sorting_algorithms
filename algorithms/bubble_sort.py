def bubble_sort(lst):
    c = 0
    for j in range(len(lst) - 1, 0, -1):
        s = False
        for i in range(j):
            one, two = lst[i], lst[i + 1]
            c += 1

            if (one > two):
                lst[i] = two
                lst[i + 1] = one
                s = True

        if not s:
            return lst, c

    return lst, c