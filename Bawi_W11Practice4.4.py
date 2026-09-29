# EMPTY DICTIONARY TUPLE

number = int(input("Enter a number: "))

bawi_students = {}

for bawi_i in range(number):
    print("\nStudent", bawi_i + 1)

    bawi_name = input("Enter Student name: ")
    bawi_g1 = float(input("Enter Grade 1: "))
    bawi_g2 = float(input("Enter Grade 2: "))
    bawi_g3 = float(input("Enter Grade 3: "))

    bawi_students[bawi_name] = [bawi_g1, bawi_g2, bawi_g3]


print("\nStudent Records:")

bawi_highest = 0
bawi_namehighest = ""

bawi_lowest = 100
bawi_namelowest = ""

bawi_tally = 0

for bawi_name, bawi_grade in bawi_students.items():

    bawi_average = sum(bawi_grade) / len(bawi_grade)

    print(bawi_name, *bawi_grade, "Average:", round(bawi_average, 2))

    if bawi_average > bawi_highest:
        bawi_highest = bawi_average
        bawi_namehighest = bawi_name

    if bawi_average < bawi_lowest:
        bawi_lowest = bawi_average
        bawi_namelowest = bawi_name

    if bawi_average > 75:
        bawi_tally += 1


print(f"\nStudent {bawi_namehighest} is highest grade: {bawi_highest:.2f}")
print(f"Student {bawi_namelowest} is lowest grade: {bawi_lowest:.2f}")
print(f"There are {bawi_tally} students with an average above 75.")
