def print_first_char(word: str) -> None:
    print(word[0])

def print_second_char(word: str) -> None:
    print(word[1])

def print_last_char(word: str) -> None:
    print(word[len(word) - 1])

print_first_char("hello")
print_second_char("hello")
print_last_char("hello")

print_first_char("test")
print_second_char("test")
print_last_char("test")
