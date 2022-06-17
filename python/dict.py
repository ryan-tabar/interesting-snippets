
person1 = {"first_name": "Ryan", "last_name": "Tabar", "age": "25", "subjects": ["science", "maths", "english"]}
person2 = {"first_name": "Ryan", "last_name": "Brown", "age": "23", "subjects": ["science", "maths", "english"]}


person3 = {}
key = (1, 2, 3, [23, 42])
stringed_key = str(key)
person3[stringed_key] = "array"

print(stringed_key)
print(person3[stringed_key])