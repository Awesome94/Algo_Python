# def revStr(str1):
# 	if len(str1) <= 1:
# 		return str1[0]
# 	else:
# 		return str1[-1] + revStr(str1[:-1])

# print(revStr("awesome"))
# print('abcdef'.center(7, '1'))
# print(list(enumerate([2,3])))
# print('abcdefcdhcd'.split('cd'))
# a = [(2,4), (1,2), (3,9)]
# a.sort()
# print('abcdef12'.replace('cd'))

def powers(x, n):
	if n == 1:
		return x
	else:
		return x * powers(x, n-1)

print(powers(10, 2))