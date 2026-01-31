import hashlib
import datetime

class User:
    def __init__(self, username, password, privilege_level):
        self.username = username
        # making password private so it is not directly accessible 
        self.__password_hash = self._hash_password(password)
        self.privilege_level = privilege_level # admin, standard, or guest
        self.login_attempts = 0
        self.account_status = "active" # active or locked
        self.activity_log = []

    def _hash_password(self, password):
        # simulating basic hashing for security
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate(self, password):
        # check if account is locked first
        if self.account_status == "locked":
            self.log_activity("Login failed: Account is locked")
            print("Account is locked. Contact admin.")
            return False

        # check password
        if self._hash_password(password) == self.__password_hash:
            print("Login successful!")
            self.reset_login_attempts() # reset attempts on succes
            self.log_activity("Login successful")
            return True
        else:
            self.login_attempts += 1
            print(f"Incorrect password. Attempts: {self.login_attempts}")
            self.log_activity("Login failed: Incorrect password")
            
            # lock account if 3 failed attempts 
            if self.login_attempts >= 3:
                self.lock_account()
            return False

    def lock_account(self):
        self.account_status = "locked"
        print(f"Alert: Account for {self.username} has been locked due to suspicious activity.")
        self.log_activity("Account locked")

    def reset_login_attempts(self):
        self.login_attempts = 0

    def check_privileges(self, required_level):
        # basic check to see if user has admin rights
        if self.privilege_level == "admin":
            return True
        if self.privilege_level == required_level:
            return True
        return False

    def log_activity(self, action):
        # logging all authentication attempts
        timestamp = datetime.datetime.now()
        self.activity_log.append(f"{timestamp}: {action}")

    def display_user_info(self):
        # display info safely without showing the password 
        print(f"User: {self.username}")
        print(f"Role: {self.privilege_level}")
        print(f"Status: {self.account_status}")
        #Password is NOT printed here

# Testing
print("--- Testing Exercise 1 ---")
# Create a standard user
user1 = User("student_john", "MySecretPass123", "standard")

# Test 1: Successful Login
user1.authenticate("MySecretPass123")

# Test 2: Failed Login multiple times to test locking
user1.authenticate("WrongPass")
user1.authenticate("WrongPass")
user1.authenticate("WrongPass") # Should lock here

# Test 3: Try to login after locking
user1.authenticate("MySecretPass123") # Should fail because it is locked