import os

def main():
    print('1 Cheapest one-way fare for given route and date')
    print('2 Cheapest one-way fare for given route and date range')
    print('3 Cheapest one-way fare for multiple destinations and date')
    print('4 Cheapest roundtrip fare for given route and date range')
    print('5 Cheapest destinations and dates for a given budget, date range, and trip duration')
    option = input('Option: ')
    print('')

    parameters = ''
    if option == '1':
        parameters = oneWaySingleDate()
    elif option == '2':
        parameters = oneWayDateRange()
    elif option == '3':
        parameters = multipleSingleDate()
    elif option == '4':
        parameters = roundTripDateRange()
    elif option == '5':
        parameters = cheapestByDateRange()
    scrape(parameters)

def oneWaySingleDate():
    origin = input('Origin (ex. MNL): ')
    destination = input('Destination (ex. HKG): ')
    departureDate = input('Departure Date (ex. 2019-01-01): ')
    parameters = '-a option=oneWaySingleDate -a origin=' + origin + ' -a destination=' + destination + ' -a departureDate=' + departureDate
    return parameters

def oneWayDateRange():
    pass

def multipleSingleDate():
    origin = input('Origin (ex. MNL): ')
    destinations = input('Comma-delimited Destinations (ex. HKG,ICN,NRT): ')
    departureDate = input('Departure Date (ex. 2019-01-01): ')
    parameters = '-a option=multipleSingleDate -a origin=' + origin + ' -a destinations=' + destinations + ' -a departureDate=' + departureDate
    return parameters

def roundTripDateRange():
    origin = input('Origin (ex. MNL): ')
    destination = input('Destination (ex. HKG): ')
    departureDate = input('Departure Date (ex. 2019-01-01): ')
    returnDate = input('Return Date (ex. 2019-01-02): ')
    parameters = '-a option=roundTripDateRange -a origin=' + origin + ' -a destination=' + destination + ' -a departureDate=' + departureDate + ' -a returnDate=' + returnDate
    return parameters

def cheapestByDateRange():
    origin = input('Origin (ex. MNL): ')
    budget = input('Budget in PHP (ex. 5000): ')
    startDate = input('Date Range Start (ex. 2019-01-01): ')
    endDate = input('Date Range End (ex. 2019-02-01): ')
    duration = input('Duration of Trip in Days: ')
    parameters = '-a option=cheapestByDateRange -a origin=' + origin + ' -a budget=' + budget + ' -a startDate=' + startDate + ' -a endDate=' + endDate + ' -a duration=' + duration
    return parameters

def scrape(parameters):
    print('Scraping...')
    os.system('scrapy runspider airscraper/spiders/search.py ' + parameters + ' --nolog')
    print('\ndepart.csv and return.csv (if applicable) generated')

main()