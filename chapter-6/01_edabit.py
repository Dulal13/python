def create_id(firstname, lastname):
    firstChar = firstname[0].lower()
    lastChar = lastname[0:3].capitalize()
    return firstChar+lastChar

a = create_id("mary", "lamb")
print(a)