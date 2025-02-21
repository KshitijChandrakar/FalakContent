import json
import os
with open("results.json", "r") as results:
    results = json.load(results)['results'][0]['result']['formatted']
    # print(results)
    for i in results:
        path = f"en/blog/{i["(B)"].strip()} - {i["(C)"].strip()}.md"
        if path == "en/blog/ - .md":
            continue
        if not os.path.exists(path): #Somehow communicate to the author that the post exists
            print(f"yea it doesnt exist, going ahead with making file {path}")
            with open(path, "w") as file:
                file.write("---\n")
                file.write(f"title: '{i["(C)"]}'\n")
                # This is commented because the date format is incorrect,  will fix that later
                #file.write(f"date: '{i["(D)"]}'\n")
                file.write(f"author: '{i["(B)"]}'\n")
                file.write("---\n")
                file.write(i["(E)"])
    pass
