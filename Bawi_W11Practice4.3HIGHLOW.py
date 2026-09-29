# HIGHEST TO LOWEST TUPLE

students = { "Ana": (90,89,94),
             "Ben": (98,89,97),
             "Carlo": (78,82,85),
             "Diana": (95,91,93) }
highest = 0
namehighest = ""
tally = 0
lowest = 100
namelowest = ""



for name, grade in students.items():
    average = sum(grade)/len(grade)
    print(f"{name}, {grade}, Average:, {average}")
    if average > highest:
        highest = average
        namehighest = name
    if average < lowest:
        lowest = average
        namelowest = name
    for g in grade:
        if g < 75:
            tally += 1
    print(f"student {namehighest} is the highest grade: ")
    print(f"student {namelowest} is lowest grade: ")
    print(f"There are {tally} students which are 75 in total.")




