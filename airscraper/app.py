import collections
import pandas as pd
import itertools
import sys
import datetime
from datetime import timedelta,date
from util import Date


def main():
	f = 1
	sdate = Date.parseDate("2019-05-25")
	edate = Date.parseDate("2019-05-30")
	duration = 3

	sum_df = pd.DataFrame(columns=['DateRange', 'Flights', 'RTFare'])

	start_date = sdate
	delta = datetime.timedelta(days=duration)
	end_date = start_date + delta
	while (start_date + delta) <= edate:
		end_date = start_date + delta

		print("for {} to {}.....".format(start_date, end_date))
		o_df = pd.read_csv('origin_data.csv')
		o_df = o_df[o_df.Date == str(start_date)]

		d_df = pd.read_csv('dest_data.csv')
		d_df = d_df[d_df.Date == str(end_date)]

		o_df.sort_values(by='Fare', inplace=True)
		d_df.sort_values(by='Fare', inplace=True)

		date_combo = [str(d1) + " to " + str(d2) for d1 in o_df['Date'] for d2 in d_df['Date']]
		flightnum_combo = [fn1 + " and " + fn2 for fn1 in o_df['FlightNumber'] for fn2 in d_df['FlightNumber']]
		fare_sum = [f1+f2 for f1 in o_df['Fare'] for f2 in d_df['Fare']]

		data = {
			'DateRange' : date_combo,
			'Flights' : flightnum_combo,
			'RTFare' : fare_sum
		}
		df = pd.DataFrame(data, columns=['DateRange', 'Flights', 'RTFare'])
		sum_df = sum_df.append(df, ignore_index = True)
		start_date += datetime.timedelta(days=1)
	
	print(sum_df.sort_values(by='RTFare'))


if __name__ == "__main__":
	main()