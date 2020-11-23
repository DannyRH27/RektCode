def count_possible_splits(arr):
    return count_possible_splits_helper(arr, 0, 0, 0)


NUM_SPLITS = 3


def count_possible_splits_helper(arr, current_index, prev_sum, split_number):
    if len(arr) - current_index < NUM_SPLITS - split_number:
        return 0

    if split_number == NUM_SPLITS - 1:
        return 1 if sum(arr[current_index:]) > prev_sum else 0

    total_counts = 0
    sum_so_far = 0
    for i in range(current_index, len(arr)):
        num = arr[i]
        sum_so_far += num
        if sum_so_far < prev_sum:
            continue

        total_counts += count_possible_splits_helper(
            arr, i + 1, sum_so_far, split_number + 1)

    return total_counts


print(count_possible_splits([9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(count_possible_splits([1, 2, 3, 4, 5, 6, 7, 8, 9]))
