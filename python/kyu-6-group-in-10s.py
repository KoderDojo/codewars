def group_in_10s(*lst_of_numbers):
    if len(lst_of_numbers) == 0:
        return []

    # place numbers into groups
    groups = {}

    for number in lst_of_numbers:
        group_index = number // 10

        group_numbers = groups.get(group_index, [])
        group_numbers.append(number)

        groups[group_index] = group_numbers

    # convert dictionary to array
    max_group_index = max(groups.keys())
    array = [None]*(max_group_index + 1)

    for k, v in groups.items():
        array[k] = sorted(v)
    return array

print(group_in_10s())

