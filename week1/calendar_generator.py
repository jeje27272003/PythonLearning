#calendar_generator.py

import calendar
while True:
	try:
		year = int(input("Enter the year: "))
		if year > 0:
			break
		else:
			print("Invalid year. Please enter a positive number.")
	except ValueError:
		print("Invalid input. Please enter a number for the year.")


while True:
	try:
		month = int(input("Enter the month: "))
		if 1 <= month <= 12:
			break
		else:
			print("Invalid number of month. Please enter a number between 1 and 12.")
	except ValueError:
		print("Invalid input. Please enter a number for the month.")

print(f"\n===== {year} {month} Calendar =====")
print("Mon Tue Wed Thu Fri Sat Sun")

# Get the number of days in the month
days = calendar.monthrange(year, month)[1]
# Get the first weekday of the month
first_weekday = calendar.monthrange(year, month)[0]


for i in range(first_weekday):
	# Print spaces for the days before the first day of the month
	print("    ", end="")

for day in range(1, days + 1):
	print(f"{day:2}", end="  ")
	if (day + first_weekday) % 7 == 0:
		print()  # New line after every 7 days

	if day == days:
		print()
