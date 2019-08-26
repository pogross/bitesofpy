from datetime import date, timedelta

TODAY = date.today()


def gen_bite_planning(num_bites=2, num_days=1, start_date=TODAY):

    num_counter = 0
    day_counter = num_days
    while True:
        if num_counter == num_bites:
            num_counter = 0
            day_counter += num_days

        yield start_date + timedelta(days=day_counter)
        num_counter += 1


if __name__ == "__main__":
    today = date.today()
    gen = gen_bite_planning(num_bites=1, num_days=1, start_date=today)
    for _ in range(10):
        print(next(gen))
