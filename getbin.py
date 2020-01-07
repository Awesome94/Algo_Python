# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    bin_lst=[]
    b_gap = 0
    for x in bin(N):
        bin_lst.append(x)
    for z in range(2, len(bin_lst)):
        j = z+1
        count = 0
        while j<len(bin_lst):
            if bin_lst[z] == '1' and bin_lst[j] == '0':
                count+=1
                j+=1
            else:
                if count > b_gap:
                    b_gap = count
                    count=0
                j+=1

    return b_gap
print(solution(1041))