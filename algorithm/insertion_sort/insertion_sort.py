

def insertion_sort(arr):
    for i in range(1, len(arr)):  # start from second element
        val = arr[i]  # store value temporarily
        j = i
        while j > 0 and arr[j - 1] > val:
            arr[j] = arr[j - 1]  # move one step
            j -= 1

        arr[j] = val


def example():
    arr = [5, 2, 4, 6, 13]
    insertion_sort(arr)
    print(arr)


if __name__ == "__main__":
    example()
