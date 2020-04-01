def caesarCipherEncryptor(string, key):
    final_str = ""
    for s in string:
        new_val = ord(s) + key
        while new_val > 122:
            mod = new_val%122
            new_val = 96+mod
        final_str+=chr(new_val)
    return final_str

print(caesarCipherEncryptor("xyz", 2))