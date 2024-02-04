
with open("/Users/HP/Desktop/python/filehandling/names/starting_names.txt") as names:
    names=names.readlines()
with open("/Users/HP/Desktop/python/filehandling/letter/starting_letter.txt") as letter:
    content=letter.read()
    for name in names:
        stripped_name=name.strip()
        contents=content.replace("[name]",stripped_name)
        with open("/Users/HP/Desktop/python/filehandling/letter/starting_letter.txt","w") as letter:
            letter.write(contents)