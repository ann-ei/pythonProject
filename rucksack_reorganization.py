def reorganize():
    input_file = open('Rucksack-Reorganization.txt', 'r')
    total = 0

    # for line in input_file:
    #     first_half = line[0:int(len(line) / 2)]
    #     print(first_half)
    #     second_half = line[int(len(line) / 2):]
    #     print(second_half)
    #
    #     founded_symbols = []
    #
    #
    #     for symb in first_half:
    #         if second_half.__contains__(symb):
    #             if founded_symbols.__contains__(symb):
    #                 continue
    #             if symb.isupper():
    #                 total += ord(symb) - 38
    #             else:
    #                 total += ord(symb) - 96
    #
    #         founded_symbols.append(symb)
    #     print(total)
    counter = 1
    for line in input_file:
        founded_symbols = []
        elves_group = []
        if counter == 1:
            first_line = line
            counter += 1
        elif counter == 2:
            second_line = line
            counter += 1
        elif counter == 3:
            third_line = line
            for symb in first_line:
                if symb == '\n':
                    continue
                else:
                    if second_line.__contains__(symb) and third_line.__contains__(symb):
                        if founded_symbols.__contains__(symb):
                            continue
                        if symb.isupper():
                            total += ord(symb) - 38
                        else:
                            total += ord(symb) - 96
                    founded_symbols.append(symb)
                    print(symb, total)
            counter = 1
    print(total)















reorganize()