languages = ['english', 'japanese', 'german', 'chinese', 'french', 'arabic']

# Print language list
print(languages)
# Now print language list alphabetically
print(sorted(languages))

# Print language list in reverse alphabetical order
print(sorted(languages, reverse=True))

# reverse the list permanently
languages.reverse()
print(languages)

# Reverse the list back to original
languages.reverse()
print(languages)

# Sort list alphabetically permanently
languages.sort()
print(languages)

# Sort and print list in reverse alphabetical order permanently
languages.sort(reverse=True)
print(languages)

# insert a new language at index 3
languages.insert(3, 'spanish')
print(languages)

# Pop to remove last index value
languages.pop()
print(languages)

# Pop a index value at given index, 0 in this case
removed_language = languages.pop(0)
print(f"{removed_language} has been removed")

# Append another value using append at the end of the list (adds another index)
languages.append('tagalog')
print(languages)

# Delete value at index 2
del languages[2]
print(languages)

# Print list values in print statement by referencing index
print(f"{languages[0].title()} is native to Germany")
print(f"In france, people speak {languages[1].title()}")
print(f"People speak traditional {languages[3].title()} in China")

# Save to variable then remove from list
language_to_remove = 'french'
removed_language_2 = languages.remove(language_to_remove)
print(f"{language_to_remove.title()} has been removed")

print(languages)
# Print the length of the list (numerical, how many values remaining, not values themselves. List length)
print(f"\nThere are {len(languages)} languages remaining")

print(f"{languages[0].title()}, {languages[1].title()}, {languages[2].title()}, and {languages[3].title()} are the remaining languages")
