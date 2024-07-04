#join method:
# list_ = ["John", "Peter", "Vicky"]
# x = " hi ".join(list_)
# print(x)

import pdb

pdb.set_trace()
def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

numbers = [1, 2, 3, 5, 6, 7, 8]
print(find_missing_number(numbers))
