import json
import os

# where we store all the tasks
FILE_NAME = "tasks.txt"


def load_tasks():
    # if file doesnt exist yet just return empty list
    if not os.path.exists(FILE_NAME):
        return []

    tasks = []
    with open(FILE_NAME, "r") as f:
        for line in f:
            line = line.strip()
            if line:  # skip empty lines
                task = json.loads(line)
                tasks.append(task)
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(json.dumps(task) + "\n")


def get_next_id(tasks):
    # just find the highest id and add 1
    if len(tasks) == 0:
        return 1
    highest = max(t["id"] for t in tasks)
    return highest + 1
