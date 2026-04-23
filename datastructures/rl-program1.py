##Manage a To DO List
to_do=["wash clothes","clean room","water plants"]
print(to_do)

## appending new task
to_do.append("walking")
to_do.append("repair tank")

## Removing Task
to_do.remove("walking")

## list of pending tasks
for task in to_do:
    print(task)
if "clean roOm".lower() in to_do:
    print("This is top priority")