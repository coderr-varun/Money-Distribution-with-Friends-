
TotalMoney = float(input("Enter the total amount of money: ₹"))
friends = int(input("Enter the number of friends: "))


share = TotalMoney / friends


for i in range(1, friends + 1):
    print(f"Friend {i} gets: ₹{share:.2f}")


print(f"\nEach friend gets {share:.2f}")
