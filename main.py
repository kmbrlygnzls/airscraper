import os

def main():
    print('1 Cheapest one-way fare for given route and date')
    print('2 Cheapest one-way fare for given route and date range')
    print('3 Cheapest one-way fare for multiple destinations and date')
    option = input('Option: ')
    print('')

    parameters = ''
    if option == "1":
        parameters = oneWaySingleDate()
    elif option == "2":
        parameters = oneWayDateRange()
    scrape(parameters)

def oneWaySingleDate():
    origin = input('Origin (ex. MNL): ')
    destination = input('Destination (ex. HKG): ')
    departureDate = input('Departure Date (ex. 2019-01-01): ')
    parameters = '-a option=oneWaySingleDate -a origin=' + origin + ' -a destination=' + destination + ' -a departureDate=' + departureDate
    return parameters

def oneWayDateRange():
    pass

def scrape(parameters):
    os.system('scrapy runspider airscraper/spiders/search.py ' + parameters + ' --nolog')

main()