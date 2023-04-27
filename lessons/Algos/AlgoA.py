num = int(input())
arr = list(map(int, input().split()))
count = 0

def merge_and_count(left, right):
    result = []
    count = 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            count += len(left) - i
    result += left[i:]
    result += right[j:]
    return result, count

def sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0
    middle = len(arr) // 2
    left, count_left = sort_and_count(arr[:middle])
    right, count_right = sort_and_count(arr[middle:])
    merged, count_merged = merge_and_count(left, right)
    return merged, count_left + count_right + count_merged

def count_inversions(arr):
    sorted_arr, count = sort_and_count(arr)
    return count, sorted_arr

count, sorted_arr = count_inversions(arr)
print(count)
print(' '.join(map(str, sorted_arr)))
