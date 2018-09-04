

def find_num(mat, target):
    for row in mat:
        if not (row[0] <= target <= row[-1]):
            continue
        if binary_search(row, target):
            return True
    return False


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            return True
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False
