"""
def find_smallest_missing_number(nums):
    sorted_nums = sorted(nums)

    smallest_missing = 1
    for num in sorted_nums:
        if num == smallest_missing:
            smallest_missing += 1
        elif num > smallest_missing:
            break

    return smallest_missing

print(find_smallest_missing_number([1, 2, 3, 4, 5, 6, 7]))"""