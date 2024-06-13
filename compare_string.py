def length_comparison_score(s1: str,
                            s2: str) -> float:
    a = len(s1)
    b = len(s2)
    if a > b:
        a, b = b, a

    gap = b - a
    if a == b:
        return 60.0
    if 2 * a <= b:
        return 0.0
    return 60.0 * (1 - gap / b)


def similarity_score(s1: str,
                     s2: str) -> float:
    total_cnt = len(set(s1) | set(s2))
    same_cnt = len(set(s1) & set(s2))
    if total_cnt == same_cnt:
        return 40.0

    return 40.0 * same_cnt / total_cnt


def compare_string(s1: str,
                   s2: str) -> float:
    if not s1.isalpha() or not s2.isalpha():
        raise ValueError("Only alphabetical inputs are allowed.")

    if not s1.isupper() or not s2.isupper():
        raise ValueError("Only capitalized inputs are allowed.")

    return length_comparison_score(s1, s2) + similarity_score(s1, s2)
