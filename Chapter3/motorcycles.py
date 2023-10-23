# Changing a specific element
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)

# Adding an element
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.append("ducati")
print(motorcycles)

# Inserting elements to a list
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, "ducati")
print(motorcycles)

# Removing elements from a list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# pop method (last element)
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# pop method (any position)
motorcycles = ["honda", "yamaha", "suzuki"]
first_motorcycle = motorcycles.pop(0)
print(first_motorcycle)

# removing an item by value
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.remove("honda")
print(motorcycles)
