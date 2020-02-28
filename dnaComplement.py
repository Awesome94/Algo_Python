import re


def dnaComplement(s):
    DNAComplimentMap = {
        'T': 'A',
        'A': 'T',
        'C': 'G',
        'G': 'C'
    }
    finalDNAString = ""
    n = len(s)-1
    for x in range(n, 0, -1):
        if s[x] in DNAComplimentMap.keys():
            finalDNAString += DNAComplimentMap[s[x]]
    return finalDNAString


print(dnaComplement('ACCGGTTTT'))
