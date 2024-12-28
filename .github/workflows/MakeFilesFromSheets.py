import json
import os
with open("results.json", "r") as results:
    results = json.load(results)['results'][0]['result']['formatted']
    # print(results)
    for i in results:
        path = f"{i["(B)"]}-{i["(C)"]}.md"
        if not os.path.exists(path) and i["(G)"].lower() in ["true", "yes", "1"] : #Somehow communicate to the author that the post exists
            with open(path, "w") as file:
                file.write("---")
                file.write(f"title: '{i["(C)"]}'")
                file.write(f"date: '{i["(D)"]}'")
                file.write(f"author: '{i["(B)"]}'")
                file.write("---")
                file.write(i["(E)"])
    pass
