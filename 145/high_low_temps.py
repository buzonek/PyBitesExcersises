from collections import namedtuple, defaultdict
import datetime
import re
import pandas as pd

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value
         
    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    # 1.Read csv
    df = pd.read_csv(DATA_FILE)
    df['Date'] = pd.to_datetime(df['Date'])

    now = datetime.datetime.now()
    # 2. Extract highest temperatures for each day / station pair between 2005-2015
    unique_stations = list(set(df['ID']))
    datelist = pd.date_range(pd.datetime(1970, 1, 1), periods=365).tolist()

    extrema_df = pd.DataFrame(columns=df.columns)
    for date in datelist:
        for station in unique_stations:
            statistics = df[(df['Date'].dt.month == date.month) & (df['Date'].dt.day == date.day) & (df['ID'] == station)]
            max_ = statistics[statistics['Element'] == 'TMAX'].max()
            min_ = statistics[statistics['Element'] == 'TMIN'].min()

    print(datetime.timedelta(datetime.now() - now))
    # 3. Remove 29th Feb
    df = df[(df['Date'].dt.month != 2) & (df['Date'].dt.day != 29)]


high_low_record_breakers_for_2015()