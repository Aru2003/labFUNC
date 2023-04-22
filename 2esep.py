def get_numbers(n):
    numbers = []
    for i in range(1, n+1):
        numbers.append(i)
    return numbers
print(get_numbers(10))


def get_student_info(student_id):
    name = "John"
    age = 22
    major = "Computer Science"
    GPA = 3.5
    if student_id == 1:
        return (name, age, major, GPA)
    else:
        return None
print(get_student_info(1))


def members(id):
    member = {
        1: {"name": "John", "age": 30, "position": "Manager", "salary": 5000},
        2: {"name": "Mary", "age": 25, "position": "Assistant", "salary": 3000},
        3: {"name": "Peter", "age": 35, "position": "Engineer", "salary": 4000}
    }
    return member.get(id)
print(members(1))