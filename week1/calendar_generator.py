#calendar_generator.py

month = input("Enter the month (1-12): ")
days = int(input("Enter the number of days in the month: "))

print(f"\n== {month} Calendar ==")
for day in range(1, days + 1):
	print(f"{day:2}", end=" ")
	if day % 7 == 0:
		print()  # New line after every 7 days

	if day == days:
		print()
