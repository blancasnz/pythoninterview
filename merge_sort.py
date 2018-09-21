
def merge(l1, l2):
    output = []

    left = 0
    right = 0

    while left < len(l1) and right < len(l2):
        if l1[left] < l2[right]:
            output.append(l1[left])
            left += 1
        else:
            output.append(l2[right])
            right += 1

    while left < len(l1):
        output.append(l1[left])
        left += 1
    while right < len(l2):
        output.append(l2[right])
        right += 1

    return output


def merge_sort(nums):
    if not nums or len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    return merge(
        merge_sort(nums[:mid]),
        merge_sort(nums[mid:])
    )
