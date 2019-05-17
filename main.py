import os

def main():
    airplane = "\n\n========================================   AirScraper   ===========================================\n\n"
    airplane += "                                               |\n"
    airplane += "                                               |\n"
    airplane += "                                               |\n"
    airplane += "                                             .-'-.\n"
    airplane += "                                            ' ___ '\n"
    airplane += "                                  ---------'  .-.  '---------\n"
    airplane += "                   ________________________'  '-'  '_________________________\n"
    airplane += "                   ''''''-|---|--/    \==][^',_m_,'^][==/    \--|---|-''''''\n"
    airplane += "                                 \    /  ||/   H   \||  \    /\n"
    airplane += "                                  '--'   OO   O|O   OO   '--'\n\n\n"
    airplane += 'Know the cheapest one-way and roundtrip fares for a given date, destination, budget, and more!\n'
    airplane += 'This scrapes data from the Cebu Pacific Airlines website, and built with Scrapy and Pandas (Python)\n\n'
    airplane += '===================================================================================================\n'
    input(airplane)

    while True:
        print('\nSelect an option below:')
        print('1 Cheapest one-way fare for given route and date')
        print('2 Cheapest one-way fare for given route and date range')
        print('3 Cheapest one-way fare for multiple destinations and date')
        print('4 Cheapest roundtrip fare for given route and date range')
        print('5 One-way fares that match the budget for a date range')
        print('6 Roundtrip fares that match the budget for a date range')
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
            parameters = oneWayByBudget()
        elif option == '6':
            parameters = cheapestByDateRange()
        elif option == 'exit':
            exit()
        scrape(parameters)
        get_results(option)
        input('\nPress Enter for next selection')

def oneWaySingleDate():
    origin = input('Origin (ex. MNL): ')
    destination = input('Destination (ex. HKG): ')
    departureDate = input('Departure Date (ex. 2019-01-01): ')
    parameters = '-a option=oneWaySingleDate -a origin=' + origin + ' -a destination=' + destination + ' -a departureDate=' + departureDate
    return parameters

def oneWayDateRange():
    origin = input('Origin (ex. MNL): ')
    destination = input('Destination (ex. HKG): ')
    departureDateFrom = input('Departure Date From (ex. 2019-01-01): ')
    departureDateTo = input('Departure Date To (ex. 2019-01-07): ')
    parameters = '-a option=oneWayDateRange -a origin=' + origin + ' -a destination=' + destination + ' -a departureDateFrom=' + departureDateFrom + ' -a departureDateTo=' + departureDateTo
    return parameters

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

def oneWayByBudget():
    origin = input('Origin (ex. MNL): ')
    budget = input('Budget in PHP (ex. 5000): ')
    departureDateFrom = input('Departure Date From (ex. 2019-01-01): ')
    departureDateTo = input('Departure Date To (ex. 2019-01-07): ')
    parameters = '-a option=oneWayByBudget -a origin=' + origin + ' -a budget=' + budget + ' -a departureDateFrom=' + departureDateFrom + ' -a departureDateTo=' + departureDateTo
    return parameters

def scrape(parameters):
    os.system('scrapy runspider airscraper/spiders/search.py ' + parameters)

def get_results(option):
    os.system('python airscraper/app.py ' + option)

main()