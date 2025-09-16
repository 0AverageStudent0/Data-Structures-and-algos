def selection(arr):
    for i in range(len(arr)-1):
        cur_min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[cur_min]:
                cur_min = j
        arr[i],arr[cur_min] = arr[cur_min],arr[i]
    return arr
def bubble(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        didswap = 0
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                didswap = 1
        if didswap == 0:
            break
    return arr
def insertion(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
    return arr
def merge(arr,low,mid,high):
    temp =[]
    left = low
    right = mid+1
    while left <= mid and right <=high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right<=high:
        temp.append(arr[right])
        right += 1
    for i in range (low,high+1):
        arr[i] = temp[i-low]
    return arr
def mergesort(arr,low,high):
        if low >= high:
            return
        mid = (low+high)//2
        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        merge(arr,low,mid,high)
        return arr
def ms (arr,n):
    high = len(arr)-1
    low = 0
    mergesort(arr,low,high)
    return arr
def quicksort(arr,low,high):
    if low<high:
        p = parti(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)
        return arr
def parti(arr,low,high):
    pivot = arr[low]
    i = low+1
    j = high

    while i<=j:
        while i <= high and arr[i] <= pivot:
            i+=1
        while j >= low and arr[j] > pivot:
            j-=1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j


arr = [4,2,5,1,3]
# print(selection(arr))
# print(bubble(arr))
# print(insertion(arr))
print(quicksort(arr,0,4))