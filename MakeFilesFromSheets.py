import json
import os
with open("results.json", "r") as results:
    results = json.load(results)['results'][0]['result']['formatted']
    # print(results)
    for i in results:
        path = f"{i["(B)"]}-{i["(C)"]}.md"
        if not os.path.exists(path) and i["(G)"].lower() in ["true", "yes", "1"]: #Somehow communicate to the author that the post exists
            print("yea it doesnt exist, going ahead with making it")
            with open(path, "w") as file:
                file.write("---\n")
                file.write(f"title: '{i["(C)"]}'\n")
                file.write(f"date: '{i["(D)"]}'\n")
                file.write(f"author: '{i["(B)"]}'\n")
                file.write("---\n")
                file.write(i["(E)"])
    pass
