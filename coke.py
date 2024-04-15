
due = 50
while due > 0:
    print("Amount owed:",due)
    coin = int(input("Insert coin: "))
    if coin in [5,10,25,50]:
        due -= coin

change = abs(due)
print("Change owed:", change)