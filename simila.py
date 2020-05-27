# def solution(A):
#     # write your code in Python 3.6
#     result = {}
#     num_pairs = 0
#     for x in range(len(A)):
#         if A[x] not in result.keys():
#             result[x] = 1
#         else:
#             result[x]+=1
#     for _, v in result.items():
#         if v > 1:
#             num_pairs +=1
#     return num_pairs

# nums = [3,5,6,3,3,5]
# print(solution(nums))


def solve(nums):
    result = []
    j = 1
    x = 0
    arr = []

    if len(nums) <= 1:
        return nums

    elif len(set(nums)) == 1:
        return [[nums[0]]*len(nums)]

    while j > x and j <= len(nums)-1:
        if nums[x] == nums[j]:
            arr.append(nums[j])
            j+=1
        else:
            arr.append(nums[x])
            result.append(arr)
            arr = []
            x = j
            j=x+1
            
    result.append(arr)
    return result

print(solve([4, 4, 1, 6, 6, 6, 1, 1, 1, 1]))