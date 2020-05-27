# def longest_substring_with_k_distinct(string, k):
#     # TODO: Write your code here
#     end = 0
#     n = len(string)
#     count = 0
#     temp_str = ""
#     final_str = ""
#     for x in range(n):
#         end = x
#         count = 0
#         while end < n:
#             if string[end] not in temp_str:
#                 count+=1
#             if count == k+1:
#                 if len(temp_str) > len(final_str):
#                     final_str = temp_str
#                 temp_str = ""
#                 break
#             temp_str+=string[end]
#             end+=1

#     return len(final_str)


def longest_substring_with_k_distinct(string, k):
    temp_str = ""
    final_len = count = 0
    n = len(string)
    for x in range(n):
        if string[x] not in temp_str:
            count+=1
            if count == k+1:
                final_len = max(len(temp_str), final_len)
                temp_str = ""
                count=0
                continue
        temp_str+=string[x]
        print(temp_str, "this is it")
    return final_len
print(longest_substring_with_k_distinct("araaci", 1))