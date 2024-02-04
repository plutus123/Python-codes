import json
website=[]
with open("./passmanager/data.json",mode="r") as data:
        dict=json.load(data)
        print(dict)
        for _ in dict:
            website.append(_)
        if e1.get() in website:
            