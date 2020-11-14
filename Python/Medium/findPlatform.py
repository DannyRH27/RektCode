def find_platform(arrival, departure):
    """
    Finds the minimum number of platforms required for a railway Station
    :param arrival: A list of arrival Timing
    :param departure: A list of departure Timing
    :return: Minimum number of platforms required for a railway Station
    """

    trains = zip(arrival, departure)
    curr_departure = departure[0]
    count = 1
    max_count = 1
    for arrival, departure in trains:
        if arrival == arrivals[0] and departure = departures[0]:
            continue

        if arrival <= curr_departure:
            count += 1
            if count > max_count:
                max_count = count
        else:
            curr_departure = departure
            count = 1
    return max_count
