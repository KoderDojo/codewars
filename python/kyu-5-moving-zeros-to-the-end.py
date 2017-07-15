import numbers


def move_zeros_mine(array):
    zero_count = 0
    new_array = []

    for i in array:
        if isinstance(i, numbers.Number) and not isinstance(i, bool) and int(i) == 0:
            zero_count += 1
        else:
            new_array.append(i)

    # add the zeros at the end
    new_array += [0]*zero_count

    return new_array


def move_zeros(array):
    return sorted(array, key=lambda x: x==2)

print(move_zeros([0, 1, None, 2, False, 1, 0]))



