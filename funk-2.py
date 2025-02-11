testgrades = [100, 90, 85, 80, 95] #input values while creating the list
for i in range(5):
    grade = int(input("Enter a grade: "))
    testgrades.append(grade)
print(testgrades)
#try to get idea for your CPT project


#student delvoped function
'''
is intened to count number of failing grades, and find highest grade
'''

def analyze_grades(listTestGrades, PassingGrade):
    numFailing = 0
    highestGrade = 0
    for grade in listTestGrades:
        if grade < PassingGrade:
            numFailing += 1
        if grade > highestGrade:
            highestGrade = grade
    return numFailing, highestGrade

#call the function
failing, highest = analyze_grades(testgrades, 70)
print("Number of failing grades: ", failing)
print("Highest grade: ", highest)