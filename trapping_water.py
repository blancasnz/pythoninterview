

def trap_dynamic(heights):
    if not heights:
        return 0

    size = len(heights)

    left = [0] * size
    left[0] = heights[0]
    for i in range(1, size):
        left[i] = max(left[i-1], heights[i])

    right = [0] * size
    right[-1] = heights[-1]
    for i in reversed(range(size-1)):
        right[i] = max(right[i+1], heights[i])

    area = 0
    for height in heights:
        area += min(left[i], right[i]) - height
    return area


def trap(height):
    area = 0

    left = 0
    right = len(height) - 1
    left_max = right_max = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] > left_max:
                left_max = height[left]
            else:
                area += left_max - height[left]
            left += 1
        else:
            if height[right] > right_max:
                right_max = height[right]
            else:
                area += right_max - height[right]
            right -= 1

    return area
