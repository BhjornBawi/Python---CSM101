# STUDENTS GR
# ADES TUPLE

students = {
    "Ana": 85,
    "Ben": 98,
    "Carlo": 78,
    "Diana": 95,
}
print("Students Grades")
print("---------------")
print("Ana: ", students["Ana"])
print("Ben: ", students["Ben"])

students["Ella"] = 88
students["Carlo"] = 82
students["Diana"] = 91

bawiname = input("Enter Student Name: ")
bawigrade = input("Enter Student Grade: ")
students[bawiname] = bawigrade

print(students)
print("\nUpdated Student Grades")
print("------------------------")

for name, grade in students.items():
    print(name, ":", grade)

while True:
    bawiname = input("Enter Student name to search: ")
    if bawiname in students:
        print(bawiname, ":", students[bawiname])
    else:
        print("Student not Found.")
    search_continue = input("Do you want to search another student? (y/n: ")
    if search_continue.lower() != "yes":
        break


