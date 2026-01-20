# list of password to test
passwords = [
    "Pass123",
    "SecurePassword1", 
    "weak",
    "MyP@ssword", 
    "NOLOWER123"
]

print("Validating passwords...")

# track the total for the final summary
compliant_count = 0
non_compliant_count = 0

for pwd in passwords:
    # reset these variables for every new pssword
    reasons = []
    has_upper = False
    has_lower = False
    has_digit = False
    
    # Check 1: Is the password at least 8 characters?
    if len(pwd) < 8:
        reasons.append("Too short")
        
    # Check 2: Look at every character to find required types    
    for char in pwd:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    # Check 3: If we never found these types, record the error        
    if has_upper == False:
        reasons.append("No uppercase")
    if has_lower == False:
        reasons.append("No lowercase letters")
    if has_digit == False:
        reasons.append("No digits")
        
    # Final Decision: If the list of errors is empty, the password passed        
    if len(reasons) == 0:
        print(f"PASS: '{pwd}' - Meets all requirements")
        compliant_count = compliant_count + 1
    else:
        # Combine all error messages in one string
        failure_msg = ", ".join(reasons)
        print(f"FAIL: '{pwd}' {failure_msg}")
        non_compliant_count = non_compliant_count + 1

print(f"Summary: {compliant_count} compliant, {non_compliant_count} non-compliant")