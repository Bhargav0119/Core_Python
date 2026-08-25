from Week_One.Day_Three.List_DayThree_Finalchallenge import sort_salaries


def test_salaries_are_sorted_in_ascending_order():
    salaries = [95000, 75000, 120000, 85000, 110000]

    ascending, _ = sort_salaries(salaries)

    assert ascending == [75000, 85000, 95000, 110000, 120000]


def test_salaries_are_sorted_in_descending_order():
    salaries = [95000, 75000, 120000, 85000, 110000]

    _, descending = sort_salaries(salaries)

    assert descending == [120000, 110000, 95000, 85000, 75000]