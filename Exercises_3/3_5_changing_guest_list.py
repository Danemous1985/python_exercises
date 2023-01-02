guests = ['caesar','spartacus','sonny liston']

print(f"Hello {guests[0].title()}, I am inviting you to dinner")
print(f"Hi {guests[1].title()}, I am inviting you to dinner")
print(f"Hey {guests[2].title()}, I am inviting you to dinner")

removed_guest = guests.pop(0)
print(f"Unfortunately, {removed_guest.title()} can no longer make it to dinner")


guests.insert(0, 'genghis khan')
print(f"Hi {guests[0].title()}, I am inviting you to dinner")
