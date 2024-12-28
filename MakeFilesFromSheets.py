<<<<<<< HEAD
import json
import os
with open("results.json", "r") as results:
    results = json.load(results)['results'][0]['result']['formatted']
    # print(results)
    for i in results:
        path = f"en/post/{i["(B)"]}-{i["(C)"]}.md"
        if not os.path.exists(path) and i["(G)"].lower() in ["true", "yes", "1"]: #Somehow communicate to the author that the post exists
            print(f"yea it doesnt exist, going ahead with making file {path}")
            with open(path, "w") as file:
                file.write("---\n")
                file.write(f"title: '{i["(C)"]}'\n")
                file.write(f"date: '{i["(D)"]}'\n")
                file.write(f"author: '{i["(B)"]}'\n")
                file.write("---\n")
                file.write(i["(E)"])
    pass
assa
=======
import json
import os
with open("results.json", "r") as results:
    results = json.load(results)['results'][0]['result']['formatted']
    # print(results)
    for i in results:
        path = f"en/post/{i["(B)"]}-{i["(C)"]}.md"
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
>>>>>>> 364ed00447a6704faa40218878e553dc79f1c232
