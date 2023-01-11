def find_elf(elves_file):
    elves_list = elves_file.read().split('\n\n')
    # for x in elves_file:
    #     elves_file.split('\n\n')
    return elves_list

def calc_sum(elf):
    elf_food = elf.split('\n')
    total = 0
    for item in elf_food:
        total += int(item)
    return total

elves_list_final = find_elf(open('elves.txt', 'r'))
max_elf1 = 0
max_elf2 = 0
max_elf3 = 0

for elf in elves_list_final:
    total = calc_sum(elf)
    if total > max_elf1:
        max_elf3 = max_elf2
        max_elf2 = max_elf1
        max_elf1 = total
    elif total > max_elf2:
        max_elf3 = max_elf2
        max_elf2 = total
    elif total > max_elf3:
        max_elf3 = total

print(max_elf1 + max_elf2 + max_elf3)


