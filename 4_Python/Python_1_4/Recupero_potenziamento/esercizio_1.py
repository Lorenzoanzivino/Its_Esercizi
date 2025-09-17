'''
Car         Hours          Charge
 1          1.5            2.00 $
 2          4.0            2.50 $
 3          24.0           10.00 $
 TOTAL      29.5           14.50 $  
 '''

total_hours = 0
total_charges = 0

def calculateCharges(hours: float) -> float:
    if hours <= 3:
        charge = 2.00
    elif hours < 24:
        charge = 2.00 + (hours - 3) * 0.5
    else:
        charge = 10.00
    return charge

cars = [(1, 1.5), (2, 4.0), (3, 24.0)]

print(f"{'Car':<10}{'Hours':<10}{'Charge':<10}")

for car_num, hours in cars:
    charge = calculateCharges(hours)
    print(f"{car_num:<10}{hours:<10}{charge} $")
    total_hours += hours
    total_charges += charge

print(f"{'TOTAL':<10}{total_hours:<10.1f}{total_charges} $")