def count_score(guide_file):
    my_total_score = 0
    # for line in guide_file:
    #     opponenst_choise = line[0]
    #     my_choise = line[2]
    #     if opponenst_choise == 'A' and my_choise == 'Y':
    #         my_total_score += 6 + 2
    #     elif opponenst_choise == 'B' and my_choise == 'Z':
    #         my_total_score += 6 + 3
    #     elif opponenst_choise == 'C' and my_choise == 'X':
    #         my_total_score += 6 + 1
    #     elif opponenst_choise == 'B' and my_choise == 'X':
    #         my_total_score += 1
    #     elif opponenst_choise == 'A' and my_choise == 'Z':
    #         my_total_score += 3
    #     elif opponenst_choise == 'C' and my_choise == 'Y':
    #         my_total_score += 2
    #     elif opponenst_choise == 'C' and my_choise == 'Z':
    #         my_total_score += 3 + 3
    #     elif opponenst_choise == 'A' and my_choise == 'X':
    #         my_total_score += 3 + 1
    #     elif opponenst_choise == 'B' and my_choise == 'Y':
    #         my_total_score += 3 + 2

    lose = 'X'
    draw = 'Y'
    win = 'Z'

    for line in guide_file:
        opponenst_choise = line[0]
        round_ending = line[2]

        if round_ending == lose:
            if opponenst_choise == 'A':
                my_total_score += 3
            elif opponenst_choise == 'B':
                my_total_score += 1
            elif opponenst_choise == 'C':
                my_total_score += 2
        elif round_ending == draw:
            if opponenst_choise == 'A':
                my_total_score += 3 + 1
            elif opponenst_choise == 'B':
                my_total_score += 3 + 2
            elif opponenst_choise == 'C':
                my_total_score += 3 + 3
        elif round_ending == win:
            if opponenst_choise == 'A':
                my_total_score += 6 + 2
            elif opponenst_choise == 'B':
                my_total_score += 6 + 3
            elif opponenst_choise == 'C':
                my_total_score += 6 + 1

    return my_total_score

print(count_score(open('rock_paper_scissors.txt', 'r')))