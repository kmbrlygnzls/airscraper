import collections
import pandas as pd
import itertools
import sys
import datetime
from datetime import timedelta, date
from util import Date


def main():
	option = sys.argv[1]
	budget = int(sys.argv[2])

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
			'RTFare' : fare_sum
		}
		sum_df = pd.DataFrame(sum_data, columns=['DateRange', 'Flights', 'RTFare'])
		print(sum_df.sort_values(by='RTFare'))

	elif option == '6':
		sum_df = pd.DataFrame(columns=['DateRange', 'Flights', 'RTFare'])
		start_date = sdate
		delta = datetime.timedelta(days=duration)
		end_date = start_date + delta
		while (start_date + delta) <= edate:
			end_date = start_date + delta

			o_df = pd.read_csv('depart.csv')
			o_df = o_df[o_df.Date == str(start_date)]

			d_df = pd.read_csv('depart.csv')
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

	elif option in ['1', '2', '3']:
		o_df = pd.read_csv('depart.csv')
		print(o_df.sort_values(by='Fare'))

	elif option == '5' and budget:
		print("option 5")
		o_df = pd.read_csv('depart.csv')
		o_df = o_df[o_df.Fare <= budget]
		print(o_df.sort_values(by='Fare'))
	


if __name__ == "__main__":
	main()