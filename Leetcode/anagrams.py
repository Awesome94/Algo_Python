def groupAnagrams(arr):
    results = {}
    for x in arr:
        sorted_str = "".join(sorted(x))
        if sorted_str in results.keys():
            results[sorted_str].append(x)
        else:
            results[sorted_str] = [x]
    return list(results.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))