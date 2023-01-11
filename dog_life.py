def count_age(dog_age):
    result = 0
    for year in range(1, dog_age + 1):
        if year == 1:
            result = 15
        elif year == 2:
            result += 9
        elif year > 2:
            result += 5

    print(result)

count_age(int(input('Enter an age')))
