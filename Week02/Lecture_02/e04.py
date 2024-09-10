def calculate_miles_per_gallon(miles_driven, gallons):
    mpg = miles_driven / gallons
    mpg = round(mpg, 1)
    return mpg

miles = 100
galns = 14
mpg = calculate_miles_per_gallon(miles, galns)

print(mpg)