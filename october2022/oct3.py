# HackerLand University has the following grading policy:

# Every student receives a  in the inclusive range from 0 to 100.
# Any grade less than  40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:

# If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            if (grades[i] + 2) % 5 == 0 or (grades[i] + 1) % 5 == 0:
                grades[i] = (round(grades[i]/5.0) * 5)
    return grades


print(gradingStudents([73, 67, 38, 33]))


