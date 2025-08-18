guest = ["Messi", "Bochini", "Newton"]

print(f"I would like to invite you, {guest[0]}")
print(f"I would like to invite you, {guest[1]}")
print(f"I would like to invite you, {guest[2]}")

print(f"\n{guest[2]}\n")

guest.remove("Newton")
guest.append("Marangoni")

print(f"I would like to invite you, {guest[0]}")
print(f"I would like to invite you, {guest[1]}")
print(f"I would like to invite you, {guest[2]}")

print(f"\nI found a bigger dinner table!\n")

guest.insert(0, "Garnero")
guest.insert(3, "Bertoni")
guest.append("Percudani")

print(f"I would like to invite you, {guest[0]}")
print(f"I would like to invite you, {guest[1]}")
print(f"I would like to invite you, {guest[2]}")
print(f"I would like to invite you, {guest[3]}")
print(f"I would like to invite you, {guest[4]}")
print(f"I would like to invite you, {guest[5]}")
