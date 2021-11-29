def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        greater = []
        less = []
        for elem in arr[1::]:
            if elem > arr[0]:
                greater.append(elem)
            else:
                less.append(elem)
        newArr = []
        newArr.extend(qsort(less))
        newArr.append(arr[0])
        newArr.extend(qsort(greater))
        return newArr


print(qsort([68, 1, 12, 3, 1, 2, 15, 6, 8]))
