locations = ['osaka','uk','rome','denmark','spain']
print(locations)

# Sorts the list alphabetically by default
print(sorted(locations))
print(locations)

# Reverse the sorted() function alphabetically
print(sorted(locations, reverse=True))
print(locations)

# Reverse the list permanently
locations.reverse()
print(locations)

# Reverse the order back to original
locations.reverse()
print(locations)

# Sort list alphabetically permanently
locations.sort()
print(locations)

# Sort list reverse alphabetically permanently
locations.sort(reverse=True)
print(locations)
