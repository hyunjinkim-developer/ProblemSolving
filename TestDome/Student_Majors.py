"""
Problem:
https://www.testdome.com/tests/python-online-test/45
"""

students = [("Allen Anderson", "Computer Science"),
            ("Edgar Einstein", "Engineering"),
            ("Farrah Finn", "Fine Arts")]

def add_new_student(students, name, major):
    students.append((name, major))

def update_student(students, index, name, major):
    students[index] = name, major

def find_students_by_name(students, name):
    return [student for student in students if name in student[0]]

def get_all_majors(students):
    return [student[1] for student in students]

# True
# In the update_student function,
# the '(' and ')' parentheses can be removed without causing any errors.
update_student(students, 0, "Jin", "CS")
print(students)

# True
# Calling find_students_by_name(students, "in") returns a list of 2 tuples.
print(find_students_by_name(students, "Jin"))
print(find_students_by_name(students, "Allen Anderson"))

# False -> Index out of range
# The add_new_student function can be rewritten as seen below
# and still maintain identical functionality
# students[len(students)] = ("Hi", "Medicine")

# False -> returns a list of 3_Greedy strings
# Calling get_all_majors(students) returns a list of 3_Greedy tuples
all_majors = get_all_majors((students))
print(all_majors)
print(type(all_majors[0]))


# The add_new_student function
# adds a new student in the last place in the list
add_new_student(students, "Minions", "Devil Followers")
print(students)

# False -> TypeError: 'tuple' object does not support item assignment
# The name of the first student in the array
# can be set to the new_name variable, like students[0][0] = new_name
students[0][0] = "Jini"
print(students)