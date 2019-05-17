import re
import datetime

class Date:
    def ParseIntMonth(monthFullString):
        monthStringMap = {
            'Jan': '01',
            'Feb': '02',
            'Mar': '03',
            'Apr': '04',
            'May': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Oct': '10',
            'Nov': '11',
            'Dec': '12'
        }
        regex = '^\S+ \| (\S*)$'
        monthString = re.search(regex, monthFullString).group(1)
        return monthStringMap[monthString]

    @staticmethod
    def parseDate(date):
        return datetime.datetime.strptime(date, '%Y-%m-%d').date()

    def GetEndDate(startDate, duration):
        date = datetime.datetime.strptime(startDate, '%Y-%m-%d')
        endDate = date + datetime.timedelta(days=int(duration))
        return endDate.strftime('%Y-%m-%d')

class Place:
    def GetAll():
        placeIDMap = {
            'REP': 'Cambodia',
            'PEK': 'Beijing',
            'HKG': 'Hong Kong',
            'CGK': 'Jakarta',
            'KIX': 'Kansai',
            'NRT': 'Tokyo',
            'MFM': 'Macau',
            'KUL': 'Kuala Lumpur',
            'SIN': 'Singapore',
            'ICN': 'Incheon',
            'TPE': 'Taipei',
            'BKK': 'Bangkok',
            'HAN': 'Hanoi'
        }
        return placeIDMap
