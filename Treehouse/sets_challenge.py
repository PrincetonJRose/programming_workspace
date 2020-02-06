COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}
# make a function that accepts a set and returns the course names that match in a list

def covers(courses):
    courses_covered = []
    for covered in COURSES:
        if courses & COURSES[covered]:
            courses_covered.append(covered)
    return courses_covered

print(covers({'Python'}))

# function that takes a set as subjects covered in the courses and returns
# only the course names that have all the subjects covered

def covers_all(subject):
    courses_covered = []
    for covered in COURSES:
        if subject <= COURSES[covered]:
            courses_covered.append(covered)
    return courses_covered

print(covers_all({"conditions", "input"}))