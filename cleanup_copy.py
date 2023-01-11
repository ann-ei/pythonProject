def is_contained(first_range, second_range):
    first_start, first_end = first_range
    second_start, second_end = second_range

    first_is_contained = first_start >= second_start and first_end <= second_end
    second_is_contained = first_start <= second_start and first_end >= second_end

    return first_is_contained or second_is_contained


def cleanup():
    ranges = []
    input_file = open('Camp-Cleanup.txt', 'r')
    total_contained = 0

    for line in input_file:
        new_arr = line[:-1].split(',')
        (first, second) = new_arr
        first_range = tuple(map(int, first.split('-')))
        second_range = tuple(map(int, second.split('-')))
        ranges.append((first_range, second_range))

        if is_contained(first_range, second_range):
            total_contained += 1
    overlaped = list(filter(is_overlaped, ranges))
    total_overlaped = len(overlaped)

    return total_contained, total_overlaped

def is_overlaped(ranges):
    first_range, second_range = ranges
    first_start, first_end = first_range
    second_start, second_end = second_range

    return second_start <= first_start <= second_end \
    or second_end >= first_end >= second_start \
    or is_contained(first_range, second_range)

# first_range, second_range
print(cleanup())