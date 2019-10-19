from typing import List

import pandas as pd

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object
df = pd.read_csv(data)

pd.options.mode.chained_assignment = None  # ignore warnings


def get_food_most_calories(df: pd.DataFrame = df):
    """Return the food "Item" string with most calories"""
    max_caloires = df.loc[df["Calories"].idxmax()]
    return max_caloires["Item"]


def get_bodybuilder_friendly_foods(
    df: pd.DataFrame = df, excl_drinks: bool = False
) -> List[str]:
    """Calulate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""
    filtered_df = df[df["Calories"] > 0].copy()
    if excl_drinks:
        filtered_df = filtered_df[
            (filtered_df.Category != "Coffee & Tea")
            & (filtered_df.Category != "Beverages")
        ]

    filtered_df["Ratio"] = filtered_df["Protein"] / filtered_df["Calories"]
    top5_df = filtered_df.nlargest(5, ["Ratio"])
    return list(top5_df["Item"])


if __name__ == "__main__":
    print(get_food_most_calories())
    print(get_bodybuilder_friendly_foods())
