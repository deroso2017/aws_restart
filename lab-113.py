# In this lab, you will:
# Use numeric data types
# Use string data types
# Use the dictionary data type
# Use the list data type
# Use a for loop
# Use the print() function
# Use the if statement
# Use the else statement
# Use the import statement

import csv
import copy

myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0,
}
myInventoryList = []

# It returns all the key–value pairs from a dictionary as something called a view object (iterable of tuples).
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

print(myVehicle.items())


with open("files/car_fleet.csv") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    print(type(csvReader))
    print(50 * "#")

    lineCount = 0  # Counter to track the number of lines processed
    for row in csvReader:
        if lineCount == 0:
            print("first row: ", row)
            print(
                f'Column names are: {", ".join(row)}'
            )  # Print the column names (join combines list elements into a string)
            lineCount += 1
        else:
            print(
                f"vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}"
            )
            # Create a deep copy of the vehicle template dictionary
            # This prevents modifying the original dictionary
            currentVehicle = copy.deepcopy(myVehicle)

            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            myInventoryList.append(currentVehicle)
            lineCount += 1
    print(f"Processed {lineCount} lines.")

print(50 * "#")

for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
        print("-----")
