#BAWI STUDENT GRADE CALCULATOR

bawi_classrec = {
        "Elson": {"StudID": "5001",
            "Grade": [90, 85, 86, 82, 83, 90, 92],
             },

        "Mark": {"StudID": "5002",
            "Grade": [51, 46, 56, 67, 55,90, 85],
                   }}

print("|==================================|")
print("| Bawi's Student Grade Calculation |")
print("|==================================|")
bawi_search = input("Enter Student Name: ").title()
if bawi_search in bawi_classrec:
        print("\033[32mThe Student has been Found!\033[0m")
        print("Student Name: ", bawi_search)
        print("StudID ",bawi_classrec [bawi_search]["StudID"])

        bawi_grades = bawi_classrec[bawi_search]["Grade"]
        print("Grades: ", bawi_grades)

        bawi_average = sum(bawi_grades) / len(bawi_grades)
        print("\nAverage: ", bawi_average)

        if min(bawi_grades) < 60:
            print("\nCandidate for Intervention.")
        else:
            print("\nNo Intervention Needed.")

        print("\nHighest Grade: ", max(bawi_grades))
        print("Lowest Grade: ", min(bawi_grades))

else:
    print("\033[31mThe Students is not Found!\033[0m")

print("|---------------|")
print("| Bawi Works <3 |")
print("|---------------|")