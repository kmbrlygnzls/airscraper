import collections
import pandas as pd
import itertools
import sys
import datetime
from datetime import timedelta, date
from util import Date


def main():
	option = sys.argv[1]
	if len(sys.argv)>=3: budget = sys.argv[2]
	if len(sys.argv)>=4: sdate = sys.argv[3]
	if len(sys.argv)>=5: edate = sys.argv[4]
	if len(sys.argv)>=6: duration = sys.argv[5]

	if option == '4':
		o_df = pd.read_csv('depart.csv')
		d_df = pd.read_csv('return.csv')

		o_df.sort_values(by='Fare', inplace=True)
		d_df.sort_values(by='Fare', inplace=True)

		date_combo = [str(d1) + " to " + str(d2) for d1 in o_df['Date'] for d2 in d_df['Date']]
		flightnum_combo = [fn1 + " and " + fn2 for fn1 in o_df['FlightNumber'] for fn2 in d_df['FlightNumber']]
		fare_sum = [f1+f2 for f1 in o_df['Fare'] for f2 in d_df['Fare']]

		sum_data = {
			'DateRange' : date_combo,
			'Flights' : flightnum_combo,
			'RTFare' : fare_sum,
			'Route' : route_combo
		}
		sum_df = pd.DataFrame(sum_data, columns=['DateRange', 'Flights', 'RTFare', 'Route'])
		print(sum_df.sort_values(by='RTFare'))

	elif option == '6':
		sum_df = pd.DataFrame(columns=['DateRange', 'Flights', 'RTFare', 'Route'])
		sdate = Date.parseDate(sdate)
		edate = Date.parseDate(edate)
		start_date = sdate
		delta = datetime.timedelta(days=int(duration))
		end_date = start_date + delta
		while (start_date + delta) <= edate:
			end_date = start_date + delta

			o_df = pd.read_csv('depart.csv')
			print(start_date)
			o_df = o_df[o_df.Date == str(start_date)]

			d_df = pd.read_csv('return.csv')
			print(end_date)
			d_df = d_df[d_df.Date == str(end_date)]

			o_df.sort_values(by='Fare', inplace=True)
			print(o_df)
			d_df.sort_values(by='Fare', inplace=True)
			print(d_df)

			date_combo = [str(d1) + " to " + str(d2) for d1 in o_df['Date'] for d2 in d_df['Date']]
			flightnum_combo = [fn1 + " and " + fn2 for fn1 in o_df['FlightNumber'] for fn2 in d_df['FlightNumber']]
			route_combo = [r1 for r1 in o_df['Route'] for r2 in d_df['Route']]
			fare_sum = [f1+f2 for f1 in o_df['Fare'] for f2 in d_df['Fare']]


			data = {
				'DateRange' : date_combo,
				'Flights' : flightnum_combo,
				'RTFare' : fare_sum,
				'Route' : route_combo
			}
			df = pd.DataFrame(data, columns=['DateRange', 'Flights', 'RTFare', 'Route'])
			sum_df = sum_df.append(df, ignore_index = True)
			start_date += datetime.timedelta(days=1)
		sum_df = sum_df[sum_df.RTFare <= int(budget)]
		print(sum_df.sort_values(by='RTFare'))

	elif option in ['1', '2', '3']:
		o_df = pd.read_csv('depart.csv')
		print(o_df.sort_values(by='Fare'))

	elif option == '5' and budget:
		print("option 5")
		o_df = pd.read_csv('depart.csv')
		o_df = o_df[o_df.RTFare <= int(budget)]
		print(o_df.sort_values(by='RTFare'))

if __name__ == "__main__":
	main()