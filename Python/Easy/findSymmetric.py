def find_symmetric(my_list):
    # Write your code here
    new_dict = {}
    for pair in my_list:
        # print(pair)
        new_dict[str([pair[1], pair[0]])] = pair

    symmetrical = []
    for pair in my_list:
        if str(pair) in new_dict:
            symmetrical.append(new_dict[str(pair)])
    return symmetrical
