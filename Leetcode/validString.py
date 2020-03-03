# []()[]
# {()[]()()[]()}


def soln(s):
    collection = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    stck = []
    for x in s:
        if not len(stck):
            stck.append(x)
        elif x != collection.get(stck[-1]):
            stck.append(x)
        else:
            stck.pop()
    print(stck)
    return not stck


print(soln("{()[]()()[]()}"))
