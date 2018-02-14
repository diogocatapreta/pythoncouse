import datetime

student = {
    "name": "Diogo",
    "birthday": datetime.date(1984,2, 15),
    "feedback": None
}

try:
    last_name = student["last_name"]
except KeyError:
    print("Error finding the last_name")

print("This code executes!")