# Import the required modules
from operator import itemgetter
import heapq

# The Map operation for counting the marks of students
def map_operation(student):
    key = student[0]
    value = student[2]
    return (key, value)

# The Reduce operation for summing up the marks of students
def reduce_operation(student_list):
    sorted_list = sorted(student_list, key=itemgetter(0))
    total_marks = 0
    result = []
    for key, group in itertools.groupby(sorted_list, key=itemgetter(0)):
        total_marks = sum(item[1] for item in group)
        result.append((key, total_marks))
    return result

# Input student list
student_list = [
    ('001', 'John', 90, 'Class A'),
    ('002', 'Sam', 85, 'Class B'),
    ('003', 'Lily', 92, 'Class C'),
    ('001', 'John', 88, 'Class A'),
    ('002', 'Sam', 78, 'Class B'),
    ('003', 'Lily', 86, 'Class C')
]

# Map operation
mapped_student_list = [map_operation(student) for student in student_list]

# Reduce operation
result = reduce_operation(mapped_student_list)

# Print the result
for item in result:
    print(f"Student roll_no: {item[0]}, Total marks: {item[1]}")