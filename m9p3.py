
def compute_mpg(miles, gallons):
    if gallons == 0:
        return 0
    return miles / gallons

trip_count = 0

response = input("Do you want to enter a trip? (Yes/No): ")

while response.lower() == "yes":
    city = input("Enter destination city: ")
    miles = float(input("Enter miles travelled: "))
    gallons = float(input("Enter gallons used: "))

    mpg = compute_mpg(miles, gallons)
    trip_count = trip_count + 1

    print("Destination:", city)
    print("Miles:", format(miles, ",.1f"))
    print("MPG:", format(mpg, ".2f"))
    print()

    response = input("Do you want to enter another trip? (Yes/No): ")

print()
print("Number of trips entered:", trip_count)