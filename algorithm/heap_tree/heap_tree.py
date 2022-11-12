class HeapTree:

    def __init__(self, priority='max'):
        self.priority = priority
        self._arr = [None]  # use from index 1

    def size(self):
        return len(self._arr) - 1

    def is_empty(self):
        return True if self.size() == 0 else False

    def get_arr(self):
        print("Heap Array:", end=' ')
        for i in range(1, self.size() + 1):
            print(self._arr[i], end=' ')
        print("\n")

    def _swap(self, a, b):
        temp = self._arr[a]
        self._arr[a] = self._arr[b]
        self._arr[b] = temp

    def insert(self, data):
        if self.is_empty():
            self._arr.append(data)
        else:
            self._arr.append(data)
            curr_idx = self.size()
            parent_idx = curr_idx

            while parent_idx > 1:
                curr_idx = parent_idx
                parent_idx = parent_idx // 2

                if (self.priority == 'max' and self._arr[curr_idx] >= self._arr[parent_idx]) or \
                   (self.priority == 'min' and self._arr[curr_idx] <= self._arr[parent_idx]):
                    self._swap(parent_idx, curr_idx)
                else:
                    break

    def delete(self):
        if self.is_empty():
            print("No root node")
        else:
            self._arr[1] = self._arr[-1]
            del self._arr[-1]
            curr_idx = 1
            while curr_idx * 2 <= self.size():  # at least one child node
                if curr_idx * 2 + 1 <= self.size():  # exist right child node
                    if self.priority == 'max':
                        if self._arr[curr_idx * 2] >= self._arr[curr_idx * 2 + 1]:
                            child_idx = curr_idx * 2
                        else:
                            child_idx = curr_idx * 2 + 1

                        if self._arr[curr_idx] < self._arr[child_idx]:
                            self._swap(curr_idx, child_idx)
                            curr_idx = child_idx
                        else:
                            break

                    elif self.priority == 'min':
                        if self._arr[curr_idx * 2] <= self._arr[curr_idx * 2 + 1]:
                            child_idx = curr_idx * 2
                        else:
                            child_idx = curr_idx * 2 + 1

                        if self._arr[curr_idx] > self._arr[child_idx]:
                            self._swap(curr_idx, child_idx)
                            curr_idx = child_idx
                        else:
                            break
                else:  # exist only left child node
                    child_idx = curr_idx * 2
                    if self.priority == 'max'and self._arr[curr_idx] < self._arr[child_idx]:
                        self._swap(curr_idx, child_idx)
                        curr_idx = child_idx
                    elif self.priority == 'min' and self._arr[curr_idx] > self._arr[child_idx]:
                        self._swap(curr_idx, child_idx)
                        curr_idx = child_idx
                    else:
                        break


def min_example():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    min_heap = HeapTree('min')
    for data in array:
        min_heap.insert(data)

    min_heap.get_arr()

    for i in range(1, min_heap.size() + 1):
        print("delete")
        min_heap.delete()
        min_heap.get_arr()


def max_example():
    print("Max Heap Example")
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    max_heap = HeapTree('max')
    for data in array:
        max_heap.insert(data)

    max_heap.get_arr()

    for i in range(1, max_heap.size() + 1):
        print("delete")
        max_heap.delete()
        max_heap.get_arr()


if __name__ == "__main__":
    min_example()
    max_example()
