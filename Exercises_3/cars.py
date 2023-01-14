cars = ['bmw', 'audi', 'toyota', 'subaru']
# Sort cars by alphabetical order
cars.sort()
print(cars)

# Sort cars in reverse alphabetical order
cars.sort(reverse=True)
print(cars)

# Sorted must be used in print statement. It is only for display
# Sorted() then print statement on new line won't work as it is only display it sorted, not re-ordering the actual list
print(sorted(cars))

# Reverse list order. This isn't reversing alphabetically, just reversing the current order
cars.reverse()
print(cars)

# Find the length of a list
len(cars)
print(len(cars))
