student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}


#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
grades = ""
for key in student_scores:
    if (student_scores[key] <= 70):
        grades = "Fail"
    elif (student_scores[key] <= 80):
        grades = "Acceptable"
    elif (student_scores[key] <= 90):
        grades = "Exceeds Expectations"
    else:
        grades = "Outstanding"
   # student_grades[key] = grades
    student_grades[key] = student_scores[key]

print(student_grades)

# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
# print(student_grades)
