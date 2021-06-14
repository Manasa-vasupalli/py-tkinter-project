import json
from utils.validators import validate_details


FILE = "./data/students.json"


def getStudents():
    try:
        with open(FILE, 'r') as file:
            return json.load(file)
    except:
        return []


def getStudentByEmail(email):
    users_list = getStudents()
    for user in users_list:
        if user['email'] == email:
            return user


def getStudentById(id):
    users_list = getStudents()
    for user in users_list:
        if user['id'] == id:
            return user


def updateStudent(id, data):
    users_list = getStudents()
    for user in users_list:
        if user['id'] == id:
            user['profile_pic'] = data['profile_pic']
            user['first_name'] = data['first_name']
            user['last_name'] = data['last_name']
            user['address'] = data['address']
            user['phone'] = data['phone']
            user['email'] = data['email']
            user['department'] = data['department']
            user['cgpa'] = data['cgpa']
    with open(FILE, "w") as file:
        json.dump(users_list, file)


def add_student(user_data):
    users_list = getStudents()  # [{...},{...}]
    user_data['id'] = len(users_list)
    users_list.append(user_data)
    with open(FILE, "w") as file:
        json.dump(users_list, file)


def check_student_exists(email):
    users_list = getStudents()  # [{...},{...}]
    for user in users_list:
        if user['email'] == email:
            return True
    return False


def check_password(email, password):
    users_list = getStudents()
    for user in users_list:
        if user['email'] == email and user['password'] == password:
            return True
    return False


def register_student(user_data):
    valid, err = validate_details(user_data)
    if not valid:
        return (False, err)
    if check_student_exists(user_data['email']):
        err = 'User with this email already exist'
        return (False, err)

    del user_data['confirm_password']
    add_student(user_data)
    return (True, None)


def login_student(email, password):
    if not check_student_exists(email):
        return (False, 'Student with this email id doesnt exist')
    if not check_password(email, password):
        return (False, 'Please enter correct password')
    return (getStudentByEmail(email)['id'], None)


def password_reset(email, password):
    users_list = getStudents()
    for user in users_list:
        if user['email'] == email:
            user['password'] = password
            break
    with open(FILE, "w") as file:
        json.dump(users_list, file)
