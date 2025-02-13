def generate_pascals_triangle(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

# Task 2: Maximum Gap

def maximum_gap(nums):
    if len(nums) < 2:
        return 0
    
    min_val, max_val = min(nums), max(nums)
    n = len(nums)
    if max_val == min_val:
        return 0
    
    bucket_size = max(1, (max_val - min_val) // (n - 1))
    bucket_count = (max_val - min_val) // bucket_size + 1
    
    buckets = [None] * bucket_count
    for num in nums:
        index = (num - min_val) // bucket_size
        if buckets[index] is None:
            buckets[index] = [num, num]
        else:
            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)
    
    max_gap = 0
    prev_max = min_val
    for b in buckets:
        if b is not None:
            max_gap = max(max_gap, b[0] - prev_max)
            prev_max = b[1]
    
    return max_gap

# Example usage:
print(generate_pascals_triangle(5))
print(maximum_gap([3,6,9,1]))
