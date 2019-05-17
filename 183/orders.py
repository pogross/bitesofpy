from os import path
from urllib.request import urlretrieve

import pandas as pd

EXCEL = path.join("tmp", "order_data.xlsx")
if not path.isfile(EXCEL):
    urlretrieve("https://bit.ly/2JpniQ2", EXCEL)


def load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""
    return pd.read_excel(excel, sheet_name="SalesOrders")


def get_year_region_breakdown(df: pd.DataFrame):
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    df["Year"] = pd.DatetimeIndex(df["OrderDate"]).year
    return df.groupby(["Year", "Region"]).sum()["Total"]


def get_best_sales_rep(df: pd.DataFrame):
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    rep_score = df.groupby(["Rep"]).sum()
    best_rep = rep_score.loc[rep_score["Total"].idxmax()]
    return best_rep.name, best_rep.Total


def get_most_sold_item(df: pd.DataFrame):
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    item_score = df.groupby(["Item"]).sum()
    best_item = item_score.loc[item_score["Units"].idxmax()]
    return best_item.name, best_item.Units
