import os
import subprocess

# Path to your VMware Workstation installation
VMWARE_PATH = "C:\\Program Files (x86)\\VMware\\VMware Workstation"
VMRUN_PATH = os.path.join(VMWARE_PATH, "vmrun.exe")

# Main function to clone and open the VM
def main():
    # Get source VM path
    source_vm_path = "C:\\Users\\nicks\\Documents\\Virtual Machines\\ParrotOS\\Parrot OS (VMware_Clone)\\Parrot OS (VMware_Clone).vmx"
   
    # Define destination path and clone name
    destination_vm_path = "C:\\Users\\nicks\\Documents\\Virtual Machines\\Clone\\Parrot_Clone.vmx"
    

    # Clone the VM
    if clone_vm(source_vm_path, destination_vm_path):
        # Start the cloned VM
        start_vm(destination_vm_path)
    else:
        print("Failed to clone the VM.")

# Function to clone the VM
def clone_vm(source_vm_path, destination_vm_path):
    if not os.path.exists(source_vm_path):
        print("Source VM not found.")
        return False
   
    # Run the vmrun command to clone the VM
    try:
        print(f"Cloning VM {source_vm_path} to {destination_vm_path}...")
        subprocess.run([VMRUN_PATH, 'clone', source_vm_path, destination_vm_path, 'full'], check=True)
        print(f"Success! Parrot VM cloned successfully to {destination_vm_path}.")
        return True
    except subprocess.CalledProcessError as error:
        print(f"Error cloning VM: {error}")
        return False

# Function to start the cloned VM in VMware Workstation
def start_vm(vm_path):
    if not os.path.exists(vm_path):
        print(f"VM path {vm_path} does not exist.")
        return False

    try:
        print(f"Starting VM {vm_path}...")
        subprocess.run([VMRUN_PATH, 'start', vm_path], check=True)
        print("VM started successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error starting VM: {e}")
        return False

if __name__ == "__main__":
    main()