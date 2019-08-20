from collections import namedtuple
from datetime import date
from typing import Tuple

import pandas as pd

DATA_FILE = "http://projects.bobbelderbos.com/pcc/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


def high_low_record_breakers_for_2015() -> Tuple[STATION, STATION]:
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a datetime.date() object.
    The temperatures in the dataset are in tenths of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.
    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day between 2005-2015
       * Extract lowest temperatures for each day between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days
    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015
    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID, Date, Value
    5. From the record breakers in 2015, extract the high/low of all the temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    df = pd.read_csv(DATA_FILE)

    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
    df["Data_Value"] = df["Data_Value"] / 10

    df = df[~((df.Date.dt.month == 2) & (df.Date.dt.day == 29))]

    df = df.pivot_table(index=["ID", "Date"], columns="Element", values="Data_Value", dropna=True)
    df.reset_index(inplace=True)

    df_2014 = df[(df.Date.dt.year >= 2005) & (df.Date.dt.year <= 2014)].copy()
    df_2015 = df[df.Date.dt.year == 2015].copy()

    df_2015["Month"] = df_2015.Date.dt.month
    df_2015["Day"] = df_2015.Date.dt.day
    df_2015.set_index(["Month", "Day"], inplace=True)

    min_record_breakers = set()
    max_record_breakers = set()
    for index, row in df_2014.iterrows():
        comp = df_2015.loc[row.Date.month].loc[row.Date.day].reset_index()

        if row.TMAX < comp.TMAX.max():
            max_row = comp.loc[comp["TMAX"].idxmax()]
            max_record_breakers.add(
                STATION(ID=max_row["ID"], Date=max_row["Date"].date(), Value=max_row["TMAX"])
            )

        if comp.TMIN.min() < row.TMIN:
            min_row = comp.loc[comp["TMIN"].idxmin()]
            min_record_breakers.add(
                STATION(ID=min_row["ID"], Date=min_row["Date"].date(), Value=min_row["TMIN"])
            )

    min_record = sorted(list(min_record_breakers), key=lambda x: x.Value)[0]
    max_record = sorted(list(max_record_breakers), key=lambda x: x.Value, reverse=True)[0]

    return max_record, min_record


if __name__ == "__main__":
    print(high_low_record_breakers_for_2015())
