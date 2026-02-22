"""
MISSION: SCOPE DETECTIVE
Identify where each variable lives: Global, Local, or Enclosing.
"""

# 1. Module-Level Variable (Global Scope)
# Accessible everywhere in this script.
BASE_SECURITY_LEVEL = 100


def initiate_system_scan(target_sector, intensity="Standard"):
    """
    Demonstrates Parameters and Local Scope.
    :param target_sector: Required Positional Parameter
    :param intensity: Parameter with a Default Value
    """
    
    # 2. Local Variable (Function Scope)
    # This variable is created when the function starts and deleted when it ends.
    scan_id = "SCAN_8821"
    
    print(f"--- Starting {intensity} scan on {target_sector} ---")
    print(f"Local Scan ID: {scan_id}")

    def generate_report(status):
        # 3. Enclosing Scope
        # This nested function can "see" variables from initiate_system_scan,
        # such as 'scan_id' and 'target_sector'.
        
        # 4. Local variable to the nested function
        report_format = ".log"
        
        print(f"Generating {status} report for {target_sector} (ID: {scan_id})")
        print(f"File format: {report_format}")

    # Calling the nested function
    generate_report(status="Success")


def process_alerts(*args, **kwargs):
    """
    Demonstrates Variadic Parameters (Args/Kwargs).
    """
    # 5. *args: Captures extra positional arguments as a Tuple
    # 6. **kwargs: Captures extra keyword arguments as a Dictionary
    
    print("\nProcessing incoming alerts...")
    
    for alert in args:
        # 7. Temporary variable (Loop Scope)
        msg = f"NOTIFICATION: {alert}"
        print(msg)

    if "user_priority" in kwargs:
        priority = kwargs["user_priority"]
        print(f"Priority override set to: {priority}")


# --- EXECUTION ---
if __name__ == "__main__":
    # Calling with a mix of positional and keyword arguments
    initiate_system_scan("Sector 7G", intensity="Deep Scan")
    
    # Calling with multiple arguments and a custom keyword
    process_alerts("CPU Overload", "Low Disk Space", user_priority="High")