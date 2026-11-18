PASS_MARK = 50


def average(grades: list[float]) -> float:
    return round(sum(grades) / len(grades), 1)


def passed(avg: float) -> bool:
    return avg >= PASS_MARK
