# --- MODULE VARIABLES ---
# These live in the global namespace of this file.
# They are accessible by any function below.
AGENCY_NAME = "Galactic Exploration Unit"
fuel_level = 100 

def prepare_shuttle(pilot_name, mission_destination="Mars", fuel_required=50):
    # --- PARAMETERS ---
    # 'pilot_name' is a required parameter.
    # 'mission_destination' is an OPTIONAL ARGUMENT with a DEFAULT value.
    
    # --- TEMPORARY VARIABLES (Local) ---
    # 'status' only exists while this function is running.
    status = f"Preparing {pilot_name} for a trip to {mission_destination}."
    
    print(f"[{AGENCY_NAME}] {status} fuel required: {fuel_required}%")
    return status

def launch_sequence(duration):
    # --- CALCULATING LIFETIME ---
    # 'countdown' is a temporary variable. 
    # Its lifetime starts when the function is called and ends when it finishes.
    for countdown in range(duration, 0, -1):
        print(f"T-minus {countdown}...")
    
    print("Liftoff!")

# --- EXECUTION (Understanding Scope) ---
prepare_shuttle("Commander Shepard") # Uses default destination
prepare_shuttle("Pilot Wash", fuel_required=100, mission_destination="Jupiter") # Uses KEYWORD argument

launch_sequence(3)