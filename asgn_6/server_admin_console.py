"""
SYSADMIN TASK: Server Management Console 

This script simulates a simple server management console for a system administrator. It allows the admin to:
 1) View the status of all servers,
 2) Update the status of a specific server, and
 3) Add new servers to the system.

It uses a event-driven design, where the user interacts with a menu to trigger different functions. 
"""

# 1. Module-Level Variable (Global Scope)
SERVERS = {
    "Web_Alpha": "Online",
    "DB_Storage": "Offline",
    "Mail_Relay": "Online"
}

def display_menu():
    """
    Function solely responsible for showing the UI.
    This separates the 'View' from the 'Logic'.
    """
    print("\n" + "="*25)
    print(">>> SYSADMIN MENU <<<")
    print("1. View All Servers")
    print("2. Change Server Status")
    print("3. Add New Server")
    print("4. Exit")
    print("="*25)

def show_status():
    print("\n--- CURRENT SERVER STATUS ---")
    # Using .items() to get key-value pairs
    for name, status in SERVERS.items():
        print(f"[{name}]: {status}")

def update_server(server_name, status="Online"):
    """
    Demonstrates Parameters with a Default Value.
    """
    # Local variable 'msg' only exists inside this function
    msg = f"Task: Setting {server_name} to {status}..."
    print(msg)
    SERVERS[server_name] = status

def add_server():
    name = input("Enter new server name: ")
    state = input("Enter initial state: ")
    SERVERS[name] = state

def main():
    """
    The Event Loop. Handles the flow of the program.
    """
    # Using 'while True' to keep the program alive
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")

        if choice == "1":
            show_status()
            
        elif choice == "2":
            target = input("Which server name?: ")
            new_val = input("Enter new status: ")
            # Passing arguments to the function
            update_server(target, new_val)
            
        elif choice == "3":
            add_server()
            
        elif choice == "4":
            print("Exiting System. Goodbye!")
            break  # This exits the 'while True' loop immediately
            
        else:
            print("Action not recognized.")

# Entry point of the script
if __name__ == "__main__":
    main()