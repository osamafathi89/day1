import json
student = {
    "name": "Osama",
    "age": 20,
    "courses": ["Math", "Science", "English"]
}
with open('files/student.json', 'w') as file:
    json.dump(student, file, indent=4)


with open('files/student.json', 'r') as file:
    data = json.load(file)
    print(data)