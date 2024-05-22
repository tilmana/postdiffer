oldRequest = open("oldrequest.txt", "r")
newRequest = open("newrequest.txt", "r")

oldData = {}
newData = {}

oldRequestData = oldRequest.readlines()[0].split("&")
newRequestData = newRequest.readlines()[0].split("&")

for value in oldRequestData:
    value = value.split("=")
    if len(value) == 2:
        oldData[value[0]] = value[1]

for value in newRequestData:
    value = value.split("=")
    if len(value) == 2:
        newData[value[0]] = value[1]

for key in oldData:
    if key in newData:
        if oldData[key] != newData[key]:
            print(f"Difference in {key}!")
            print(f"{oldData[key]} / {newData[key]}")

diffCount = abs(len(oldData) - len(newData))
print(f"[!] Skipped {diffCount} parameters due to difference in count between request bodies!")
