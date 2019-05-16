import re
from datetime import date,datetime

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
        return datetime.strptime(date, '%Y-%m-%d').date()

class Place:
    def GetAll():
        placeIDMap = {
            'DAC': 'Bangladesh',
            'BWN': 'Brunei',
            'REP': 'Cambodia',
            'PEK': 'Beijing',
            'CAN': 'Guangzhou',
            'PVG': 'Shanghai',
            'HKG': 'Hong Kong',
            'DPS': 'Bali',
            'CGK': 'Jakarta',
            'FUK': 'Fukuoka',
            'NGO': 'Nagoya',
            'KIX': 'Kansai',
            'CTS': 'Hokkaido',
            'NRT': 'Tokyo',
            'MFM': 'Macau',
            'BKI': 'Kota Kinabalu',
            'KUL': 'Kuala Lumpur',
            'SIN': 'Singapore',
            'ICN': 'Incheon',
            'PUS': 'Busan',
            'TPE': 'Taipei',
            'BKK': 'Bangkok',
            'HAN': 'Hanoi',
            'SGN': 'Ho Chi Minh'
        }
        return placeIDMap
