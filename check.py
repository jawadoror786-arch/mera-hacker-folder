p = input("Password likho: ")
if len(p) < 6:
    print("WEAK! Boht chota hai Ror!")
elif len(p) < 10:
    print("Medium hai, thoda or bara karo")
else:
    print("STRONG! Hacker bhi nahi tor payega!")
