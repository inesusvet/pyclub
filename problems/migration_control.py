"""
Given a list of date periods when a foreign person was in the country.
When today date is passed,
Then required to answer the question: "How many days in last 6 months this
person spend in the country?" Day of coming in is counting as one and the day
of leaving the country is counting as one
"""

from datetime import date, datetime, timedelta


example = """
04.06.2018 - 01.07.2018
12.07.2018 - 15.07.2018
16.08.2018 - 23.08.2018
08.09.2018 - 13.09.2018
26.09.2018 - 30.09.2018
21.10.2018 - 23.10.2018
31.10.2018 - 03.11.2018
04.11.2018 - 29.11.2018
30.11.2018 - 05.12.2018
"""

def main(periods, today, n_days):
    return 0


if __name__ == '__main__':
    today = date(2018, 12, 05)
    cleaned = example.strip()
    lines = cleaned.split('\n')

    periods = []
    for line in lines:
        start, end = line.split(' - ')
        start = datetime.strptime(start, '%d.%m.%Y')
        end = datetime.strptime(end, '%d.%m.%Y')
        periods.append((start, end))

    print main(periods, today, 180)
