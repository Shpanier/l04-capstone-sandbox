from grades import average, median, passed


def test_average_and_pass_mark():
    assert average([100, 55]) == 77.5
    assert passed(60)
    assert not passed(59.9)


def test_median():
    assert median([70, 90, 80]) == 80
    assert median([60, 70]) == 65
