import os

def main():
    print '1 Cheapest one-way fare for given route and date'
    print '2 Cheapest one-way fare for given route and date range'
    option = raw_input('Option: ')
    print ''

    parameters = ''
    if option == "1":
        parameters = oneWaySingleDate()
    elif option == "2":
        parameters = oneWayDateRange()
    scrape(parameters)

def oneWaySingleDate():
    origin = raw_input('Origin (ex. MNL): ')
    destination = raw_input('Destination (ex. HKG): ')
    departureDate = raw_input('Departure Date (ex. 2019-01-01): ')
    parameters = '-a option=oneWaySingleDate -a origin=' + origin + ' -a destination=' + destination + ' -a departureDate=' + departureDate
    return parameters

def oneWayDateRange():
    pass

def scrape(parameters):
    os.system('scrapy runspider airscraper/spiders/search.py ' + parameters + ' --nolog')

main()