arrival = [17 , 978, 409, 229, 934, 299, 982, 636, 14 , 866, 815, 64 , 537, 426, 670, 116, 95 , 630]
duration = [17 , 502, 518, 196, 106, 405, 452, 299, 189, 124, 506, 883, 753, 567, 717, 338, 439, 145]


# arrival = [5, 1, 1, 1, 1, 4]
# duration = [5, 10, 3, 6, 4, 2]
def maxEvents(arrival, duration):
    # Write your code here

    sortedCompanies = zip(arrival, duration)
    sortedCompanies.sort(key=lambda x: x[0])
    print(sortedCompanies)
    
    eventCounter = 0
    departure = 0
    currentPresenterArrivalTime = 0
    for i in range(len(arrival)):    
        # print(sortedCompanies[i], eventCounter, departure, currentPresenterArrivalTime, sortedCompanies[i][0], sortedCompanies[i][1])
        currDeparture = sortedCompanies[i][0] + sortedCompanies[i][1]
        # print('before if check', sortedCompanies[i][0], currentPresenterArrivalTime, departure)
        if sortedCompanies[i][0] >= departure:
            currentPresenterArrivalTime = sortedCompanies[i][0]
            departure = currDeparture
            eventCounter += 1
        elif currDeparture < departure:
            print('hit here')
            departure = min(departure, currDeparture)
        
    return eventCounter

print(maxEvents(arrival, duration))
