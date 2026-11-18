PASS_MARK = 60


def average(grades: list[float]) -> float:
    return round(sum(grades) / len(grades), 1)


def passed(avg: float) -> bool:
    return avg >= PASS_MARK


def median(grades: list[float]) -> float:
    s = sorted(grades)
    m = len(s) // 2
    return s[m] if len(s) % 2 else (s[m - 1] + s[m]) / 2
