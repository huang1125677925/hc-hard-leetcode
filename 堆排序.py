#encoding=utf-8
def buildMaxHeap(arr):
    # 这建的是大根堆
    for i in range(len(arr)//2,-1,-1):
        heapify(arr,i)

def buildMinHeap(arr):
    # 这建的是大根堆
    for i in range(len(arr)//2,-1,-1):
        heapify(arr,i)

def heapify(arr, i):
    left = 2*i+1
    while left < arrLen:
        if left + 1 < arrLen and arr[left+1] > arr[left]:
            left = left+1
        arr[left], arr[i] = arr[i], arr[left]
        i = left
        left = left*2 +1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    return arr




# ----------------------------------
def minHeapify(arr, heapsize, index):
    left = 2 * index + 1
    mini = index
    while left < heapsize:
        if left+1 < heapsize and arr[left] > arr[left+1]:
            left = left+1
        if arr[index] > arr[left]: arr[index], arr[left] = arr[left], arr[index]
        index = left
        left = 2*index +1


def buildMinHeap_1(list):
    heapSize = len(list)
    if heapSize < 2:
        return
    for i in range(heapSize / 2 - 1, -1, -1):
        minHeapify(list, heapSize, i)


def heapSort_1(list):
    buildMinHeap_1(list)
    for i in range(len(list) - 1, -1, -1):
        list[0], list[i] = list[i], list[0]
        minHeapify(list, i, 0)
    return list




print(heapSort([1,9,0,-1,-4,43,100]))
print(heapSort_1([1,9,0,-1,-4,43,100, 1000]))


