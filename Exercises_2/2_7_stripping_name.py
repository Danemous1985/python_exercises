first_name = " dane "
last_name = " goulter "
print(f"{first_name} {last_name}")
# Whitespace is stripped. .title() added to capitalize. lstrip() and rstrip() can also be used here
full_name = f"Name:\n\t{first_name.strip().title()}\n\t{last_name.strip().title()}"
print(f"{full_name}")