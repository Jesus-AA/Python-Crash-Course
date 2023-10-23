cars = ["bmw", "audi", "toyota", "subaru"]

# Sort alphabetically permanently sort()
cars.sort(reverse=True)
print(cars)

# Temporary Sort sorted()
cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Printing in reverse order
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.reverse()
print(cars)

print(len(cars))
