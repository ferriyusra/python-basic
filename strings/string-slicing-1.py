def get_substring(input_string: str, start: int, end: int) -> str:
    if end > len(input_string):
        return ""
    
    return input_string[start:end]

print(get_substring("FerriYus", 1, 7))
print(get_substring("FerriYus", 1, 8))
print(get_substring("FerriYus", 1, 9))
print(get_substring("FerriYus", 0, 2))
print(get_substring("FerriYus", 0, 7))
print(get_substring("FerriYus", 4, 8))
