

arr = [170, 45, 75, 90, 802, 24, 2, 66]


def radix_sort(arr):
    base_10 = []
    for i in range(10):
        base_10.append([])
    temp = []
    for i in range(10):
        temp.append([])
    x = True
    y = max(arr)
    d = 1
    while x:

        if y / 10 > 1:
            d += 1
            y = y / 10

        else:
            x = False
            break
    # base_10[0].append("aa")
    # print(base_10)

    for j in range(d):
        output = []
        base_10 = []
        for i in range(10):
            base_10.append([])
        for i in arr:
            x = i % 10**(j+1)
            x = x // 10**j
            base_10[x].append(i)
        for l in base_10:
            output.extend(l)

        arr = output

    return arr


print(radix_sort(arr))


