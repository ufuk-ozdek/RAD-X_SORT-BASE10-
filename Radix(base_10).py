arr = [170, 45, 75, 90, 802, 24, 2, 66]


def radix_sort(arr):
    x = True
    y = max(arr)
    d = 1
    while x:
        if y / 10 > 1:
            d += 1
            y = y / 10
        else:
            break
    for j in range(d):
        output = []
        base_10 = [[]for i in range(10)]
        for i in arr:
            k = i % 10**(j+1)
            k = k // 10**j
            base_10[k].append(i)
        for l in base_10:
            output.extend(l)

        arr = output

    return arr


print(radix_sort(arr))

