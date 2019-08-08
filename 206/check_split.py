from typing import Tuple
from decimal import Decimal, ROUND_DOWN


def check_split(item_total: str, tax_rate: str, tip: str, people: int) -> Tuple[str, list]:
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    total = Decimal(item_total.strip("$"))
    tax_percent = Decimal(tax_rate.strip("%")) / 100
    tip_percent = Decimal(tip.strip("%")) / 100

    total_taxed = (total * (1 + tax_percent)).quantize(Decimal(".01"))
    grand_total = (total_taxed * (1 + tip_percent)).quantize(Decimal(".01"))

    split = (grand_total / people).quantize(Decimal(".01"), rounding=ROUND_DOWN)
    splits = [split] * people
    splits[0] += grand_total - sum(splits)

    print(sum(splits))
    return (f"${grand_total}", splits)
