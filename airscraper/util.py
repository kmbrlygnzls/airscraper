import re

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