students = [
    {
        "id":1,
        "name": "Rahul",
        "email": "rahul@gmail.com",
        "age" : 21,
        "course" : "Mechanical"
    },
    {
        "id": 2,
        "name": "Ravi",
        "email": "ravi@gmail.com",
        "age": 25,
        "course": "Robotics"
    },
    {
        "id":3,
        "name": "Suneendra",
        "age":28,
        "email":"suneendrabsa@gmail.com",
        "course":"Backend Engineering"
    }
]


def get_all_students():
    return students


def get_student_by_id(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return None

def create_student(student_data: dict):
    student_data["id"] = len(students) + 1
    students.append(student_data)
    return student_data


def update_student(student_id: int, updated_data: dict):

    student = get_student_by_id(student_id)

    if student:
        student.update(updated_data)
        return student

    return None

def delete_student(student_id: int):
    student = get_student_by_id(student_id)

    if student:
        students.remove(student)
        return True

    return False

# repository layer  = data access = - find / create/ update/ delete