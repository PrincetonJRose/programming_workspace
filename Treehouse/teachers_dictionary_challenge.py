# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

# show total number of teachers
def num_teachers(dict):
    return len(dict.keys())

# show total number of courses between all teachers
def num_courses(dict):
    num_courses = 0
    for value in dict.values():
        num_courses += len(value)
    return num_courses

# show only the courses taught in the dictionary
def courses(dict):
    course = []
    for classes in dict:
        for clas in dict[classes]:
            course.append(clas)
    return course
    
# show only the name of the teacher who teaches the most amount of courses
def most_courses(dict):
    count = []
    for teacher in dict:
        count.append(len(dict[teacher]))
    most = max(count)
    for teacher in dict:
        if most == len(dict[teacher]):
            return teacher

# show the names of the teachers and how many courses they teach in a list with lists
def stat(dict):
    stat_count = []
    teacher_count = 0
    for teacher in dict:
        stat_count.append([teacher])
        stat_count[teacher_count].append(len(dict[teacher]))
        teacher_count += 1
    return stat_count
