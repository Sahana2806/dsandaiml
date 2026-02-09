student={"name":"sahana","age":22,"course":"MCA","marks":85}
print(student["name"])
print(student["marks"])

student={"name":"sahana","age":22,"course":"MCA","marks":85}
print(student.keys())

print(student.values())

print(student.items())

print(student.get("age"))
print(student.get("grade"))

student.update({"age":22,"grade":"A"})
print(student)

student.pop("course")
print(student)

student.clear()
print(student)

student={"name":"sahana","age":22,"course":"MCA","marks":85}
new_student=student.copy()
print(new_student)

student.setdefault("marks",90)
print(student)

keys=["a","b","c"]
new_dict=dict.fromkeys(keys,0)
print(new_dict)

