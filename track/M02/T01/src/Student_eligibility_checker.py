#Student Eligiblity checker
# Read marks, attendance and project completion status
marks = int(input())
attendence = int(input())
Project_Completion = input()

# Check the academic requirements
if (marks >= 60 and attendence >= 75):
    # Check the project completion status
    if (Project_Completion == "yes"):
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")