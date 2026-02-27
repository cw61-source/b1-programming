import json


class UserStore:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        users = []
        try:
            with open(self.file_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        users.append(json.loads(line))
        except FileNotFoundError:
            # file doesn't exist yet, just return empty list
            pass
        return users

    def save(self, users):
        with open(self.file_path, "w") as f:
            for user in users:
                f.write(json.dumps(user) + "\n")

    def find_by_id(self, user_id):
        users = self.load()
        for user in users:
            if user["id"] == user_id:
                return user
        return None

    def update_user(self, user_id, updated_data):
        users = self.load()
        for i, user in enumerate(users):
            if user["id"] == user_id:
                # merge in the new fields but keep the id intact
                users[i].update(updated_data)
                users[i]["id"] = user_id
                self.save(users)
                return True
        return False

    def delete_user(self, user_id):
        users = self.load()
        filtered = [u for u in users if u["id"] != user_id]
        if len(filtered) == len(users):
            return False  # nothing was removed
        self.save(filtered)
        return True
