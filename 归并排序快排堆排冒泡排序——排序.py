#encoding=utf-8
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left,right=arr[:mid],arr[mid:]
    return merge(mergeSort(left),mergeSort(right))


def merge(left,right):
    result=[]
    for i in range(len(left)):
        for j in range(len(right)):
            if left[i] <= right[j]:
                print [left[i], right[j]]
    while len(left)>0 and len(right)>0:
        if left[0]<right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    if left:
        result.extend(left)
    if right:
        result.extend(right)
        
    return result

def OriginMergeSort(arr, l, r):
    if l < r:
        mid = (l+r)//2
        OriginMergeSort(arr, l, mid)
        OriginMergeSort(arr, mid+1, r)
        Merge(arr, l, mid, r)

def Merge(arr, l, mid, r):
    result = []
    le,re = l, mid+1
    while le <= mid and re <= r:
        if arr[le] < arr[re]:
            result.append(arr[le])
            le +=1
        else:
            result.append(arr[re])
            re+=1

    while le <= mid:
        result.append(arr[le])
        le+=1
    while re <= r:
        result.append(arr[re])
        re+=1
        
    arr[l:r+1] = result

# 这个不是原地排序
def quicksort(arr):
    if len(arr) >= 2:
        temp = arr[0]
        # 每次都选第一个值为中枢结点， 分成左右两块
        left = [i for i in arr[1:] if i <= temp]
        right = [i for i in arr[1:] if i > temp]
    elif len(arr) == 1:
        # 如果数组小于1，就没有什么排列需要了
        return arr
    else:
        return []
    
    return quicksort(left) + [temp] + quicksort(right)

# print(quicksort([5, 7, 8, 10, 90, 100, 200, 3, -1]))
arr = [0,1,-9,100,34,87,2,-100,93,200]
# print(OriginMergeSort(arr, 0, len(arr)-1))
# #这个不是原地排序
# print arr
print mergeSort(arr)

