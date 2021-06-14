import json
from utils.students_utils import getStudents, updateStudent
from utils.validators import validate_details, validate_details_no_pass
FILE = "./data/requests.json"


def getRequests():
    try:
        with open(FILE, 'r') as file:
            return json.load(file)
    except:
        return []


def update_request(student_data):
    students = getRequests()
    updated = False
    for i in range(len(students)):
        if students[0]['id'] == student_data['id']:
            students[i] = student_data
            updated = True
    if not updated:
        students.append(student_data)
    with open(FILE, "w") as file:
        json.dump(students, file)


def createRequest(student_data={}):
    valid, err = validate_details_no_pass(student_data)
    if not valid:
        return (False, err)
    if not 'id' in student_data:
        return (False, "No Id passed")
    update_request(student_data)
    return (True, None)

def getRequest(id):
    students = getRequests()
    for student in students:
        if student['id'] == id:
            return student

def mergeRequest(id):
    updateStudent(id, getRequest(id))
    deleteRequest(id)


def deleteRequest(id):
    students = getRequests()
    new_students = list(filter(lambda x: x['id'] != id, students))
    with open(FILE, "w") as file:
        json.dump(new_students, file)
