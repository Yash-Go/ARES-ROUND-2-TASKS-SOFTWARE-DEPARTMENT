# Section - Python Question 1.1

# M1 by using built in functions

readings = [10, 12, 11, 50, 13]

total = sum(readings)
no_of_readings = len(readings)

average = total / no_of_readings
print(f"This is the average taken out by using formulas: {average}")

# M2 by using core logic

readings = [10, 12, 11, 50, 13]

total = 0
no_of_readings = 0

for i in readings:
    total += i
    no_of_readings += 1

new_average = total / no_of_readings

print(f"This is the average taken out without using formulas: {new_average}")
