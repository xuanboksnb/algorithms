def heapify(array, n):
    for i in range(n / 2 - 1, -1, -1):
        heap(array, i, n)


def heap(array, inode, n):
    # n = len(array)
    l = 2 * inode + 1
    r = 2 * inode + 2
    if l < n:
        m = array[l]
        s = l
        if r < n:
            if array[r] > m:
                m = array[r]
                s = r
        if array[inode] < m:
            array[inode], array[s] = array[s], array[inode]
            heap(array, s, n)


def sort(array):
    array = list(array)
    n = len(array)
    heapify(array, len(array))
    n -= 1
    array[0], array[n] = array[n], array[0]
    while n > 0:
        heap(array, 0, n)
        n -= 1
        array[0], array[n] = array[n], array[0]
    return array


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = [4, 1, 7, 2, 5, 6, 3, 8]
    # heap(a, 0)
    print sort(a)
    print a
