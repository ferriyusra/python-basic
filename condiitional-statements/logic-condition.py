def discount_applies(age: int) -> bool:
    if age < 18 or age >= 65:
        return True
    return False

print(discount_applies(23))
print(discount_applies(40))
print(discount_applies(65))
