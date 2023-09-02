def find_cycle(num):
    residues = []
    next_residue = 1
    decimal_representation = "0."
    while (next_residue != 0) and (next_residue not in residues):
        residues.append(next_residue)
        while next_residue < num:
            next_residue *= 10
        decimal_representation += str(next_residue // num)
        next_residue = next_residue % num
    if next_residue == 0:
        return decimal_representation, 0
    cycle_start = residues.index(next_residue)
    cycle_length = len(residues) - cycle_start
    decimal_representation = decimal_representation[:-cycle_length] + '(' + decimal_representation[-cycle_length:] + ')'
    return decimal_representation, cycle_length


max_cycle = 0
max_d = 1
for d in range(2, 1000):
    curr_cycle = find_cycle(d)[1]
    if curr_cycle > max_cycle:
        max_cycle = curr_cycle
        max_d = d

# The answer is 983
print(f"Best d: {max_d}, with length: {max_cycle}")
