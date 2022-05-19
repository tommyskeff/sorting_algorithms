def merge_sort(lst, c=0):
    if len(lst) < 2:
        return lst, c

    mid = len(lst) // 2
    first = lst[:mid]
    second = lst[mid:]

    c = merge_sort(first, c)[1]
    c = merge_sort(second, c)[1]

    i = 0
    j = 0
    k = 0

    while i < len(first) and j < len(second):
        c += 1
        if first[i] < second[j]:
            lst[k] = first[i]
            i += 1
        else:
            lst[k] = second[j]
            j += 1
        k += 1

    while i < len(first):
        lst[k] = first[i]
        i += 1
        k += 1

    while j < len(second):
        lst[k] = second[j]
        j += 1
        k += 1

    return lst, c