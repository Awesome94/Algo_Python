def twos_complement(input_value: int, num_bits: int) -> int:
    mask = 2 ** (num_bits - 1)
    return -(input_value & mask) + (input_value & ~mask)


print(twos_complement(3, 1))