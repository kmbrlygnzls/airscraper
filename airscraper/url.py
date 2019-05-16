from airscraper.util import Date
from datetime import timedelta,date
class UrlService:
    urlList = []

    @staticmethod
    def setUrlList(origin, destination, dateRangeFrom, dateRangeTo):
        if dateRangeTo:
            startDate = Date.parseDate(dateRangeFrom)
            endDate = Date.parseDate(dateRangeTo)
            
            for date in range(int ((endDate - startDate).days)+1):
                newDate =  startDate + timedelta(date)
                UrlService.addUrl(origin,destination,newDate)

    @staticmethod
    def addUrl(origin,destination,departureDate):
        UrlService.urlList.append('https://book.cebupacificair.com/Flight/Select?o1={0}&d1={1}&dd1={2}'.format(origin,destination,departureDate))

    @staticmethod
    def getUrlList():
        return UrlService.urlList