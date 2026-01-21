# def two_sum(nums, target):
#     # Dictionary to store value: index
#     dict = {}
#
#     for i, n in enumerate(nums):
#         diff = target - n
#         if diff in dict:
#             return [dict[diff], i]
#         else:
#             dict[n] = i
#     return
#
# nums = [2, 7, 11, 15]
# target = 13
# call=print(two_sum(nums,target))

l1 = ['r', 'b', 'w', 'r', 'b', 'w', 'r', 'b', 'w', 'r', 'b', 'w']
def occureneces(l1):
    l1 = ['r', 'b', 'w', 'r', 'b', 'w', 'r', 'b', 'w', 'r', 'b', 'w']

    # Step 1: Count occurrences using a dictionary
    counts = {}
    for char in l1:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    # Step 2: Rebuild the list in the specific order: 'r', 'b', 'w'
    result = []
    for char in ['r', 'b', 'w']:
        if char in counts:
            # Use list multiplication to add the character 'n' times
            result.extend([char] * counts[char])

    print(result)
    # Output: ['r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'w', 'w', 'w', 'w']
call=occureneces(l1)