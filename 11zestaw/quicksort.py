import module


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def partition(arr, l, s):
    i = l - 1
    x = arr[s]

    for j in range(l, s):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[s] = arr[s], arr[i + 1]
    return i + 1


def quicksort(array, l, r):

    stack = Stack()
    stack.push(-1)
    stack.push(l)
    stack.push(r)

    while len(stack.items) >= 2:

        r = stack.pop()
        l = stack.pop()

        p = partition(array, l, r)

        if p-1>l:
            stack.push(l)
            stack.push(p-1)
        if p+1<r:
            stack.push(p+1)
            stack.push(r)


array = module.randomList(10)
print("Przed sortowaniem: ", array)
quicksort(array, 0, len(array)-1)
print("Po sortowaniu: ", array)