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
