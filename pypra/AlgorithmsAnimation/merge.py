def merge(array, start, mid, end):
    n1 = mid-start+1
    n2 = end-mid

    left = [None]*n1
    right = [None]*n2

    for x in range(0, n1):
        left[x] = array[start+x]

    for x in range(0, n2):
        right[x] = array[mid+1+x]

    i = 0
    j = 0
    k = start
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = right[j]
        j += 1
        k += 1

def merge_sort(array, start, end):
    if start < end:
        mid = start+(end-start)/2

        merge_sort(array, start, mid)
        merge_sort(array, mid+1, end)

        merge(array, start, mid, end)


array = [12,10,3,9,6,8,2]
print (array)
merge_sort(array, 0, len(array)-1)
print(array)