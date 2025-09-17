import json


text = input("Enter students and gpas: ")


students = []


for entry in text.split(","):
    entry = entry.strip()  
    if not entry:
        continue
    name, gpa = entry.split()
    student = {"name": name, "gpa": float(gpa)}
    students.append(student)


print(json.dumps(students, indent=4))


with open("students.json", "w") as f:
    json.dump(students, f, indent=4)
