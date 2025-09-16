cnt = 0
def mergesort(arr, low, high):
    if low >= high:
        return 0  # base case: no inversions in a single element

    mid = (low + high) // 2
    cnt = 0

    # Recursively count inversions in left and right halves
    cnt += mergesort(arr, low, mid)
    cnt += mergesort(arr, mid + 1, high)
    cnt += countpairs(arr,low,mid,high)
    # Count inversions while merging both halves
    merge(arr, low, mid, high)

    return cnt

def countpairs(arr,low,mid,high):
    right = mid+1
    cnt = 0
    for i in range(low,mid+1):
                while (right <= high and arr[i] > 2*arr[right]):
                    right += 1
                cnt += (right - (mid+1))
    return cnt
def merge(arr,low,mid,high):
    left = low
    right = mid+1
    temp = []
    while left <= mid and right <= high:
        if arr[left] <= arr[right]: 
            temp.append(arr[left])
            left += 1
        else: 
            temp.append(arr[right])
            right += 1
    while left <= mid :
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(low,high+1):
        arr[i] = temp[i-low]


arr = [3,2,1]
print(mergesort(arr, 0, len(arr) - 1))

