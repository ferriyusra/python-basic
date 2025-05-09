def concatenate(s1: str, s2: str) -> str:
    concatenation = s1 + s2
    
    if len(concatenation) <= 10:
        return concatenation
    
    return "Too long!"

print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
