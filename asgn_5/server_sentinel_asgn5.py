FAIL_STATUS = "failed"

# --- Task 1: File Interaction ---
def load_logs(filename):
    logs = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            logs.append(tuple(parts))
    return logs
   

def get_failed_actions(logs):
    failed_actions = []
    for entry in logs:
        if entry[3] == FAIL_STATUS:  # entry[3] is status
            failed_actions.append(entry[1])  # entry[1] is username
    return failed_actions


def count_user_actions(logs):
    user_counts = {}
    for entry in logs:
        username = entry[1]
        user_counts[username] = user_counts.get(username, 0) + 1
    return user_counts

# --- Task 3: Exporting Results ---
def save_summary(counts, filename="server_sentinel_summary_asgn5.txt"):
    with open(filename, 'w') as file:
        file.write("SERVER ACTIVITY SUMMARY\n")
        file.write("========================\n")
        for user, count in counts.items():
            file.write(f"User: {user} | Actions: {count}\n")
    print(f"Summary successfully saved to {filename}")

# --- Main Execution ---
def main():
    # 1. Load data from the file
    server_log_file = input("Enter the server log filename: ")
    data = load_logs(server_log_file)
    
    if data:
        failed_list = get_failed_actions(data)
        activity_counts = count_user_actions(data)
        
        print(f"Processed {len(data)} entries.")
        if "admin" in failed_list:
            print("Warning: Admin failures detected!")
            
        server_summary_file = input("Enter the filename to save the summary (or press Enter to use default): ")
        if server_summary_file.strip() == "":
            server_summary_file = "server_sentinel_summary_asgn5.txt"
        save_summary(activity_counts, server_summary_file)
    else:
        print("No data found in the log file.")

if __name__ == "__main__":
    main()