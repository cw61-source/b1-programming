devices = [
    ("192.168.1.10", [22, 80, 443]),
    ("192.168.1.11", [21, 22, 80]), 
    ("192.168.1.12", [23, 80, 3389])
]

risky_ports = [21, 23, 3389]

print("Scanning network devices...")

risk_count = 0

for device in devices:
    ip_address = device[0]
    open_ports = device[1]
    
    #We are now inside one specific device nd we need to loop through that device's list of ports
    for port in open_ports:

        #comparing the current port found on th device against the list of bad ports defined at the top
        if port in risky_ports:
            print(f"WARNING: {ip_address} has risky port {port} open")
            risk_count = risk_count + 1

print(f"Scan complete: {risk_count} security risks found")