def falling_boxes(box):
    if len(box) == 0 or len(box[0]) == 0:
        return []

    num_rows = len(box)
    num_cols = len(box[0])
    post_gravity = []
    for _ in range(num_rows):
        post_gravity.append(['.'] * num_cols)
    print(post_gravity)
    for i in range(num_rows):
        row = box[i]
        last_seen_obstacle = num_cols
        for j in reversed(range(num_cols)):
            if row[j] == '.':
                continue

            if row[j] == '*':
                last_seen_obstacle = j
                post_gravity[i][j] = '*'
                continue

            # only pounds are left
            last_seen_obstacle -= 1
            post_gravity[i][last_seen_obstacle] = '#'

    # now that we ran gravity, we do the rotation to present it properly
    result = []
    for i in range(num_cols):
        row = []
        for j in range(num_rows):
            row.append(post_gravity[j][i])
        result.append(list(reversed(row)))

    return result


box = [
    ['#', '#', '.', '.', '*'],
    ['.', '.', '#', '#', '#'],
]
# print(falling_boxes(box))

# [
#     ['.', '.', '#', '#', '*'],
#     ['.', '.', '#', '#', '#'],
# ]

# =>

# [
#     ['.', '.'],
#     ['.', '.'],
#     ['#', '#'],
#     ['#', '#'],
#     ['#', '*'],
# ]

box2 = [['#', '#', '.', '*', '.', '.', '.'],
       ['#', '#', '#', '.', '.', '.', '.'],
       ['#', '#', '#', '.', '.', '#', '.']]
# print(falling_boxes(box2))
falling_boxes(box2)

# rotateAndFall(box) = [['.', '.', '.'],
# ['.', '.', '#'],
# ['.', '.', '#'],
# ['#', '.', '*'],
# ['#', '#', '.'],
# ['#', '#', '.'],
# ['#', '#', '.']]
