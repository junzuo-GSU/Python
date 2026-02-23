import os

PROD_SUFFIX = "-prod"
DEV_SUFFIXES = ("-dev", "-lab")
PRODUCTION = "Production"
DEVELOPMENT = "Development"
UNKNOWN = "Unknown"

def get_server_list(filename):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        print("Current working directory:", os.getcwd())
        return []
     
    server_list = []
    with open(filename, 'r') as file:
        for line in file:
            server_list.append(line.strip())
    return server_list
    

def identify_server_type(server_name):
    if server_name.endswith("-prod"):
        return "Production"
    elif server_name.endswith("-dev") or server_name.endswith("-lab"):
        return "Development"
    else:
        return "Unknown"


def display_report(servers):
    print("--- SERVER INVENTORY REPORT ---")
    for name in servers:
        status = identify_server_type(name)
        print(f"Server: {name:15} | Type: {status}")
    print("-------------------------------")

def main():
    server_name_file = input("Enter the filename containing server names: ")
    server_names = get_server_list(server_name_file)
    
    if server_names:
        display_report(server_names)
    else:
        print("No server names found in the file.")    

if __name__ == "__main__":
    main()