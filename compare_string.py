def compare_string(s1: str,
                   s2: str) -> float:
    if not s1.isalpha() or not s2.isalpha():
        raise ValueError("Only alphabetical inputs are allowed.")

    if not s1.isupper() or not s2.isupper():
        raise ValueError("Only capitalized inputs are allowed.")

    if len(s1) > len(s2):
        s1, s2 = s2, s1

    a = len(s1)
    b = len(s2)
    gap = b - a

    if a == b:
        return 60.0

    if 2 * a <= b:
        return 0.0

    return 60.0 * (1 - gap / b)

