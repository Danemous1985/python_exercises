name = "ada lovelace"
# .title() function capitalises the first letters
print(name.title())
# .upper prints as uppercase
print(name.upper())
#.lower prints as lowercase
print(name.lower())

first_name = "ada"
last_name = "lovelace"
# Assign both variables above to a single variable (full_name)
# f"" not in brackets as is not a print statement
full_name = f"{first_name} {last_name}"
print(full_name)
# f"" in brackets as is print statement
print(f"Hello, {full_name.title()}!")

# assign full_name to a variable and message. Then print after
message = f"Hello, {full_name.title()}!"
print(message)

# Add a tab to a string with \t
print("\tPython")
# Add a new line with \n
print("Language:\nPython\nJavascript\nC")
# Add a newline, then a tab with \n\t
print("Language:\n\tPython\n\tJavascript\n\tC")

# String with whitespace
favourite_language = "python "
# rstrip() strips the whitespace at the endtemporarily. "python " to "python"
favourite_language.rstrip()
print(favourite_language.title())
# Reassign favourite_language variable so the whitespace is stripped permanently
favourite_language = favourite_language.rstrip()
print(favourite_language.title())\
# lstrip() to strip from left side, or strip() to strip from both sides
favourite_language = favourite_language.strip()
print(favourite_language.title())
