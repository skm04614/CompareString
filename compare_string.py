def compare_string(s1: str,
                   s2: str) -> int:
    if not s1.isalpha() or not s2.isalpha():
        raise ValueError("Only alphabetical inputs are allowed.")

    if not s1.isupper() or not s2.isupper():
        raise ValueError("Only capitalized inputs are allowed.")

    return 0
