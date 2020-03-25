class Solution:
    def rotate(self, arr: List[List[int]]) -> None:
        arr_map = {}
        visted = []
        dr = len(arr[0])
        for r in range(len(arr)):
            j = 0
            dc=0
            dr -= 1
            
            while j < len(arr) and dr >= 0:
                arr_map[str(r), str(j)] = [dc, dr]
                j+=1
                dc+=1

        for k, _ in arr_map.items():
            r = int(k[1])
            c = int(k[0])
            temp = [arr[c][r], c, r]

            while temp[1:] not in visted:
                num = temp[0]
                visted.append(temp[1:])
                result = arr_map[str(temp[1]), str(temp[2])]
                temp = [arr[result[0]][result[1]], result[0], result[1]]
                arr[result[0]][result[1]] = num

        return arr
        

arr = [[1,2,3,10],[4,5,6,11],[7,8,9,12]]

print(rotate(arr))

{('0', '0'): [0, 2], ('0', '1'): [1, 2], ('0', '2'): [2, 2], ('1', '0'): [0, 1], ('1', '1'): [1, 1], ('1', '2'): [2, 1], ('2', '0'): [0, 0], ('2', '1'): [1, 0], ('2', '2'): [2, 0]}