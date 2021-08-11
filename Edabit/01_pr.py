def top_note(student):
    n = student['name']
    top = max(student["notes"])
    return {'name': n , 'top_notes':top}
a = top_note({ "name": "John", "notes": [3, 5, 4] })
print(a)
