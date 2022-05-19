def quick_sort(lst, c = 0):
    less = []
    equal = []
    greater = []

    if len(lst) > 1:
        pivot = lst[0]
        for x in lst:
            c += 1
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)

        less = quick_sort(less, c)
        c = less[1]
        less = less[0]

        greater = quick_sort(greater, c)
        c = greater[1]
        greater = greater[0]

        return less + equal + greater, c
    else:
        return lst, c