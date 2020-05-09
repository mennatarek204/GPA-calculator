# new dictionary to save keys with their right values
score_map = {
    'A+' : 4,
    'A' : 3.83,
    'A-' : 3.66,
    'B+' : 3.33,
    'B' : 3,
    'B-' : 2.66,
    'C+' : 2.33,
    'C' : 2,
    'C-' : 1.66,
    'D+' : 1.33,
    'D' : 1,
    'F' : 0,
}

#lists of needed data
grades = []
CreditHours = []

#function to collect and calculate user inputs
def collect():
    t = int(input("enter number of terms: "))
    c = int(input("enter number of courses: "))
    overall_GPA =0
    for i in range(t):
        print("\nenter courses of term %d " % (i+1))
        for j in range(c):
            course_name = input("\nenter course name %d: " % (j+1))
            grade_letters = input("enter grade letters %d: " % (j+1))
            grades.append(grade_letters)
            credit = int(input("enter credit hour %d: " % (j+1)))
            CreditHours.append(credit)
            GPA = sum(score_map[grade_letters]*credit for grade_letters in grades) / sum(CreditHours)
            overall_GPA+=GPA
        print("GPA of term %d = " % (i+1), GPA)
    overall_GPA =overall_GPA/t
    print("The overall GPA = ", overall_GPA)
    if 3.6<=overall_GPA<=4:
        print("The Final Grade is Excellent")
    elif 3<=overall_GPA<=3.6:
        print("The Final Grade is Very Good")
    elif 2.6<=overall_GPA<=3:
        print("The Final Grade is Good")
    else:
        print("The Final Grade is Pass")
print(collect())