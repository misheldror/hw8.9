# START

slices: int = int(input("how many slices? "))

eaten = slices // 4
left = slices % 4

print(f"each one ate- {eaten}")
print(f"slices left- {left}")

# END

# START

people: int = int(input("how many friends? "))
slices: int = int(input("how many slices? "))

eaten = slices // people
left = slices % people

print(f"each one ate- {eaten}")
print(f"slices left- {left}")

# END
