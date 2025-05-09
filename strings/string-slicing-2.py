def first_n_characters(s: str, n: int) -> str:
    return s[:n]

def last_n_characters(s: str, n: int) -> str:
    start = len(s) - n
    return s[start:]

print(first_n_characters("FerriYus", 3))
print(first_n_characters("FerriYus", 4))
print(first_n_characters("FerriYus", 8))

print(last_n_characters("FerriYus", 3))
print(last_n_characters("FerriYus", 4))
print(last_n_characters("FerriYus", 8))
