import datetime

class Device:
    def __init__(self, device_id, device_type, owner):
        self.device_id = device_id
        self.device_type = device_type
        self.owner = owner
        self.firmware_version = "1.0"
        self.compliance_status = True # compliant or not
        self.is_active = True
        # Set last scan to today initially
        self.last_security_scan = datetime.datetime.now()
        self.logs = []

    def update_firmware(self, new_version):
        self.firmware_version = new_version
        self.log_action(f"Firmware updated to {new_version}")

    def run_security_scan(self):
        print(f"Scanning device {self.device_id}...")
        self.last_security_scan = datetime.datetime.now()
        self.compliance_status = True
        self.log_action("Security scan completed")

    def check_compliance(self):
        # Check if scan was more than 30 days ago 
        days_since_scan = (datetime.datetime.now() - self.last_security_scan).days
        if days_since_scan > 30:
            self.compliance_status = False
            self.log_action("Device marked non-compliant: Scan overdue")
            return False
        return True

    def quarantine(self):
        # Method to quarantine compromised device
        self.is_active = False
        self.compliance_status = False
        self.log_action("Device quarantined")
        print(f"Device {self.device_id} has been quarantined.")

    def log_action(self, action):
        # All device interactions logged with timestamps 
        timestamp = datetime.datetime.now()
        self.logs.append(f"{timestamp}: {action}")

class DeviceManager:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"Device {device.device_id} added to network.")

    def authorise_access(self, user, device):
        # Logic: Check ownership and complianc
        
        # 1.Check if device is active/compliant
        if not device.compliance_status:
            # Allow admin override [cite: 200]
            if user.privilege_level == "admin":
                print(f"ADMIN OVERRIDE: Accessing non-compliant device {device.device_id}")
                device.log_action(f"Admin {user.username} accessed non-compliant device")
                return True
            else:
                print(f"Access Denied: Device {device.device_id} is non-compliant.")
                return False

        # 2.Check ownership
        if device.owner == user.username or user.privilege_level == "admin":
            print(f"Access Granted to {device.device_id}")
            device.log_action(f"User {user.username} accessed device")
            return True
        else:
            print("Access Denied: You do not own this device.")
            return False

#Testing the System
print("\n--- Testing Exercise 2 ---")
# Create users from Exercise 1
admin_user = User("admin_alice", "admin123", "admin")
std_user = User("student_bob", "bob123", "standard")

# Create a device owned by Bob
my_thermostat = Device("IOT-101", "Thermostat", "student_bob")

# Create Manager
manager = DeviceManager()
manager.add_device(my_thermostat)

# Test 1: Bob accesses his own device 
manager.authorise_access(std_user, my_thermostat)

# Test 2: Simulate time passing to make device not compliant
# Manually setting date to 31 days ago for testing
my_thermostat.last_security_scan = datetime.datetime.now() - datetime.timedelta(days=35)
my_thermostat.check_compliance() # Updates status to False

# Test 3: Bob tries to access non compliant device
manager.authorise_access(std_user, my_thermostat)

# Test 4: Admin tries to access non compliant device
manager.authorise_access(admin_user, my_thermostat)