def pay_bill(balance: int, bill: int) -> int:
    if balance >= bill:
        balance = balance - bill
    return balance

print(pay_bill(100, 50))
print(pay_bill(100, 100))
print(pay_bill(100, 150))
