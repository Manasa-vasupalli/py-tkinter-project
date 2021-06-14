# m1 = int(input())
# m2 = int(input())
# a = m2/m1
# n = int(input())
# print("%.3f"%(a**(n-2)))

from utils.request_utils import createRequest, deleteRequest, mergeRequest


p = {
    'a': 1
}

# print('a' in p)

print(createRequest({
    "profile_pic": "C:/Users/Manasa/OneDrive/Pictures/p2pdops.png",
    "first_name": "manu",
    "last_name": "aaa",
    "address": "Universe",
    "phone": "6303822152",
    "email": "p2pdops@gmail.com",
    "password": "nopassword",
    "department": "CSE",
    "cgpa": "8.0",
    "id": 1
}))

# mergeRequest(1)