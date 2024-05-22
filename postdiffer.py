oldRequest = open("oldrequest.txt", "r")
newRequest = open("newrequest.txt", "r")

oldData = {}
newData = {}
diffData = []

oldRequestData = oldRequest.readlines()[0].split("&")
newRequestData = newRequest.readlines()[0].split("&")

for value in oldRequestData:
    value = value.split("=", 1)
    if len(value) == 2:
        oldData[value[0]] = value[1]

for value in newRequestData:
    value = value.split("=", 1)
    if len(value) == 2:
        newData[value[0]] = value[1]

for key in oldData:
    if key in newData:
        if oldData[key] != newData[key]:
            diffData.append(key)
            print(f"=====Difference in {key}!=====")
            print(f"{oldData[key]} / {newData[key]}")

print(f"Differing parameters: {diffData}")
if oldData.keys() - newData.keys():
    print(f"Keys only in old request: {oldData.keys() - newData.keys()}")
else:
    print("No difference in keys between old request versus new request")
if newData.keys() - oldData.keys():
    print(f"Keys only in new request: {newData.keys() - oldData.keys()}")
else:
    print("No difference in keys between new request versus old request")
