# Step 1: Define a list of doctor types
doctor_types = [
    "General Practitioner",
    "Cardiologist",
    "Dermatologist",
    "Pediatrician",
    "Neurologist"
]

# Step 2: Function to display doctor types and get user selection
def select_doctor_type():
    print("Select the type of doctor you need:")
    for i in range(len(doctor_types)):
        print(f"{i + 1}. {doctor_types[i]}")
    while True:
        choice = int(input("Enter the number corresponding to your choice: "))
        if 1 <= choice <= len(doctor_types):
            return doctor_types[choice - 1]
        else:
            print("Invalid choice. Please try again.")

# Step 3: Collect patient details
def get_patient_details():
    name = input("Enter your name: ")
    contact = input("Enter your contact information: ")
    return name, contact

# Step 4: Collect appointment time
def get_appointment_time():
    time = input("Enter the appointment time (e.g., 10:00 AM, 2:30 PM): ")
    return time

# Step 5: Store appointment details in a dictionary and add to list
def create_appointment():
    doctor_type = select_doctor_type()
    name, contact = get_patient_details()
    time = get_appointment_time()
    appointment = {
        "patient_name": name,
        "contact": contact,
        "doctor_type": doctor_type,
        "appointment_time": time
    }
    return appointment

# Step 6: Store appointments in a list
appointments = []

# Step 7: Function to display appointments
def display_appointments():
    if not appointments:
        print("No appointments booked yet.")
    else:
        print("Appointments:")
        for i in range(len(appointments)):
            appointment = appointments[i]
            print(f"{i + 1}. {appointment['patient_name']} with {appointment['doctor_type']} at {appointment['appointment_time']}")

# Main function to run the program
def main():
    while True:
        print("\nWelcome to Health Genius")
        print("1. Book an Appointment")
        print("2. View Appointments")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            appointment = create_appointment()
            appointments.append(appointment)
            print("Appointment booked successfully!")
        elif choice == '2':
            display_appointments()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
 