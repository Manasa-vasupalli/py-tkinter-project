import re

mail_re = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
phone_re = '^\d{10}$'


def is_valid_email(email):
    return bool(re.search(mail_re, email))


def is_valid_phone(phone):
    return bool(re.search(phone_re, phone))


def is_valid_password(password):
    return len(password) >= 8 and len(password) <= 15


def validate_details(user_data):
    first_name = user_data['first_name']
    last_name = user_data['last_name']
    address = user_data['address']
    phone = user_data['phone']
    email = user_data['email']
    password = user_data['password']
    confirm_password = user_data['confirm_password']
    department = user_data['department']
    cgpa = user_data['cgpa']

    err = ''
    if(len(first_name) < 3):
        err += 'Enter valid first name\n'
    if(len(first_name) < 3):
        err += 'Enter valid first name\n'
    if(len(last_name) < 3):
        err += 'Enter valid last name\n'
    if(len(address) < 4):
        err += 'Enter valid address\n'
    if(not is_valid_phone(phone)):
        err += 'Enter valid phone number (10 digits)\n'
    if(not is_valid_email(email)):
        err += 'Enter valid email address\n'
    if(not is_valid_password(password)):
        err += 'Enter valid password >8 chars\n'
    if(password != confirm_password):
        err += 'Password and confirm password should be same\n'

    try:
        print(float(cgpa))
        if float(cgpa) < 0.0 and float(cgpa) > 10.0:
            err += 'Enter a valid CGPA\n'
    except:
        print(cgpa)
        err += 'Enter a valid CGPA\n'

    return (len(err) == 0, err.strip())


# mdetails = {'first_name': 'Manasa',
#             'last_name': 'Vasupalli',
#             'address': 'Heaven',
#             'phone': '630382200',
#             'email': 'manasavasupalli2000gmail.com',
#             'password': 'Manasa12',
#             'confirm_password': 'Manasa123'
#             }

# print(validate_details(mdetails))

mail_re = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
phone_re = '^\d{10}$'


def is_valid_email(email):
    return bool(re.search(mail_re, email))


def is_valid_phone(phone):
    return bool(re.search(phone_re, phone))


def is_valid_password(password):
    return len(password) >= 8 and len(password) <= 15


def validate_details_no_pass(user_data):
    profile_pic = user_data['profile_pic']
    first_name = user_data['first_name']
    last_name = user_data['last_name']
    address = user_data['address']
    phone = user_data['phone']
    email = user_data['email']
    cgpa = user_data['cgpa']

    err = ''
    if(len(profile_pic) < 3):
        err += 'Select a profile picture\n'
    if(len(first_name) < 3):
        err += 'Enter valid first name\n'
    if(len(last_name) < 3):
        err += 'Enter valid last name\n'
    if(len(address) < 4):
        err += 'Enter valid address\n'
    if(not is_valid_phone(phone)):
        err += 'Enter valid phone number (10 digits)\n'
    if(not is_valid_email(email)):
        err += 'Enter valid email address\n'
    try:
        print(float(cgpa))
        if float(cgpa) < 0.0 and float(cgpa) > 10.0:
            err += 'Enter a valid CGPA\n'
    except:
        print(cgpa)
        err += 'Enter a valid CGPA\n'

    return (len(err) == 0, err)


def validate_details(user_data):
    _, err = validate_details_no_pass(user_data)
    password = user_data['password']
    confirm_password = user_data['confirm_password']

    if(not is_valid_password(password)):
        err += 'Enter valid password >8 chars\n'
    if(password != confirm_password):
        err += 'Password and confirm password should be same\n'

    return (len(err) == 0, err.strip())


# mdetails = {'first_name': 'Manasa',
#             'last_name': 'Vasupalli',
#             'address': 'Heaven',
#             'phone': '630382200',
#             'email': 'manasavasupalli2000gmail.com',
#             'password': 'Manasa12',
#             'confirm_password': 'Manasa123'
#             }

# print(validate_details(mdetails))
