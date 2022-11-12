#!/usr/bin/python3


def parent(i):
    return (i - 1) // 2 + 1


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def heapify(priority, arr, i, size):
    l = left(i)
    r = right(i)

    if priority == 'max':
        if l <= size and arr[l] > arr[i]:
            largest = l
        else:
            largest = i
        if r <= size and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            swap(arr, i, largest)
            heapify(priority, arr, largest, size)

    elif priority == 'min':
        if l <= size and arr[l] < arr[i]:
            smallest = l
        else:
            smallest = i
        if r <= size and arr[r] < arr[smallest]:
            smallest = r

        if smallest != i:
            swap(arr, i, smallest)
            heapify(priority, arr, smallest, size)


def build_heap(priority, arr):
    size = len(arr) - 1
    for i in range(parent(size), 0, -1):  # bottom-up to index 1
        heapify(priority, arr, i, size)


def heap_sort(priority, arr):
    arr.insert(0, None)
    length = len(arr) - 1
    size = length
    build_heap(priority, arr)
    for i in range(length, 1, -1):  # bottom-up to index 2
        swap(arr, i, 1)
        size = size - 1
        heapify(priority, arr, 1, size)
    del arr[0]
    return arr


def example():
    unsorted_arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

    sorted_arr = heap_sort('max', unsorted_arr)
    print(sorted_arr)


if __name__ == "__main__":
    example()
