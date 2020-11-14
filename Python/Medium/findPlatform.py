def find_platform(arrival, departure):
    """
    Finds the minimum number of platforms required for a railway Station
    :param arrival: A list of arrival Timing
    :param departure: A list of departure Timing
    :return: Minimum number of platforms required for a railway Station
    """

    trains = list(zip(arrival, departure))
    curr_departure = departure[0]
    count = 1
    max_count = 1
    for train in trains:
        if train == trains[0]:
            continue
        arrival = train[0]
        departure = train[1]

        if arrival <= curr_departure:
            count += 1
            if count > max_count:
                max_count = count
        else:
            curr_departure = departure
            count = 1
    return max_count
