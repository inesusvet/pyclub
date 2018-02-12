"""
See https://www.codewars.com/kata/cat-years-dog-years/

I have a cat and a dog.
I got them at the same time as kitten/puppy. That was `humanYears` years ago.

Return their respective ages now as (`humanYears`, `catYears`, `dogYears`)

NOTES:
- humanYears >= 1

### Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that

### Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
"""


def human_years_cat_years_dog_years(human_years):
    return human_years, cat_years, dog_years


def test():
    assert human_years_cat_years_dog_years(1) == (1, 15, 15)
    assert human_years_cat_years_dog_years(2) == (2, 24, 24)
    assert human_years_cat_years_dog_years(10) == (10, 56, 64)


test()
