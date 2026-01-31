import logging

# Configure logging to print warnings to console as welll
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def analyze_logs():
    print("Starting Log Analysis...")
    
    # Track failed logins for brute force detection
    failed_logins = {} 

    try:
        with open("server.log", "r") as log_file, \
             open("error_log.txt", "w") as error_file, \
             open("security_incidents.txt", "w") as security_file: 
            for line in log_file:
                try:
                    # Basic parsing by splitting spaces 
                
                    parts = line.split()
                    
                    if len(parts) < 9:
                        continue # Skip malformed lines

                    ip_address = parts[0]
                    # Status code is usually the 9th item 
                    status_code = int(parts[8]) 
                    
                    #Task 1: Error Logs (4XX and 5XX)
                    if status_code >= 400 and status_code < 600:
                        error_file.write(line)

                    #Task 2: Security Monitoring 
                    incident_found = False
                    reason = ""

                    # Check 1: Suspicious User Agents 
                    # check the raw line because 'split' breaks the user agent string
                    if "sqlmap" in line or "curl" in line:
                        incident_found = True
                        reason = "Suspicious User Agent"

                    # Check 2: Failed Authentication (401)
                    if status_code == 401:
                        incident_found = True
                        reason = "Failed Authentication"
                        
                        # Count failures for Brute Force detection 
                        if ip_address in failed_logins:
                            failed_logins[ip_address] += 1
                        else:
                            failed_logins[ip_address] = 1

                    # Write to security file if incident found 
                    if incident_found:
                        security_file.write(f"INCIDENT: {reason} | IP: {ip_address} | Status: {status_code}\n")
                        logging.warning(f"Security Alert: {reason} detected from {ip_address}") # 

                except ValueError:
                    # Handle malformed lines where status code isn't a number
                    logging.error(f"Could not parse status code in line: {line[:20]}...")
                    continue

            #Post-Analysis: Check for Brute Force
            security_file.write("\n--- BRUTE FORCE ANALYSIS ---\n")
            for ip, count in failed_logins.items():
                if count >= 2: # Threshold for "repeated failures" 
                    msg = f"Potential Brute Force: {ip} had {count} failed login attempts."
                    security_file.write(msg + "\n")
                    logging.warning(msg)

            print("Analysis complete. Check 'error_log.txt' and 'security_incidents.txt'.")

    except FileNotFoundError:
        print("Error: 'server.log' not found.")
    except Exception as e:
        print(f"Critical Error: {e}")

if __name__ == "__main__":
    analyze_logs()