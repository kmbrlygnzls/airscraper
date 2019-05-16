import collections
import pandas as pd
import itertools


def main():
	o_df = pd.read_csv('origin_data.csv')
	d_df = pd.read_csv('dest_data.csv')

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
	sum_df.to_json(r'C:\Users\kgonzales\airscraper\airscraper\sorted_data.json', orient='records')


if __name__ == "__main__":
	main()