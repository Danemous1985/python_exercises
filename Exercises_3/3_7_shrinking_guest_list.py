guests = ['caesar','spartacus','sonny liston']

print(f"Hello {guests[0].title()}, I am inviting you to dinner")
print(f"Hi {guests[1].title()}, I am inviting you to dinner")
print(f"Hey {guests[2].title()}, I am inviting you to dinner")

removed_guest = guests.pop(0)
print(f"\nUnfortunately, {removed_guest.title()} can no longer make it to dinner")


guests.insert(0, 'genghis khan')
print(f"\nHi {guests[0].title()}, I am inviting you to dinner")

print("\nI have found a bigger table, so will be inviting more guests\n")

guests.insert(0, 'abraham lincoln')
guests.insert(2, 'gandalf the grey')
guests.append('bilbo baggins')

print(f"Hi {guests[0].title()}, you are now also invited for dinner")
print(f"{guests[2].title()}, is now also invited for dinner")
print(f"Finally, {guests[-1].title()} will also be attending\n")

print(f"The dinner table will not arrive in time, so I must shrink the guest list to two guests only")

removed_1 = guests.pop(0)
removed_2 = guests.pop(3)
removed_3 = guests.pop(2)
removed_4 = guests.pop(0)
print(f"The following guests will no longer be attending. {removed_1.title()},{removed_2.title()},{removed_3.title()},{removed_4.title()}.")

print(f"\n{guests[0].title()} and {guests[1].title()} are still invited to dinner")

del guests[0]
del guests[0]
print(f"The last two guests have been deleted also {guests}")
