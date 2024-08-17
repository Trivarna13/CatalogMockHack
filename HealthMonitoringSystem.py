import json
import os

class HealthMonitoringSystem:
    def __init__(self, data_file='patient_records.json'):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                try:
                    self.records = json.load(file)
                except json.JSONDecodeError:
                    self.records = {}
        else:
            self.records = {}

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.records, file)

    def add_patient_record(self):
        patient_id = input("Enter Patient ID: ")
        blood_pressure = input("Enter Blood Pressure: ")
        cholesterol = input("Enter Cholesterol: ")
        diagnosis_data = {'blood_pressure': blood_pressure, 'cholesterol': cholesterol}
        self.records[patient_id] = diagnosis_data
        self.save_data()
        print("Patient record added successfully.")

    def retrieve_patient_record(self):
        patient_id = input("Enter Patient ID to retrieve: ")
        if patient_id in self.records:
            print(f"Patient Record for {patient_id}: {self.records[patient_id]}")
        else:
            print("Patient record not found.")

    def update_medical_record(self):
        patient_id = input("Enter Patient ID to update: ")
        if patient_id in self.records:
            print(f"Current Record: {self.records[patient_id]}")
            blood_pressure = input("Enter new Blood Pressure: ")
            cholesterol = input("Enter new Cholesterol: ")
            self.records[patient_id]['blood_pressure'] = blood_pressure
            self.records[patient_id]['cholesterol'] = cholesterol
            self.save_data()
            print("Patient record updated successfully.")
        else:
            print("Patient record not found.")

    def delete_patient_record(self):
        patient_id = input("Enter Patient ID to delete: ")
        if patient_id in self.records:
            del self.records[patient_id]
            self.save_data()
            print("Patient record deleted successfully.")
        else:
            print("Patient record not found.")

    def menu(self):
        while True:
            print("\nAutomatic Health Monitoring System:")
            print("1. Add Patient Record")
            print("2. Retrieve Patient Record")
            print("3. Update Medical Record")
            print("4. Delete Patient Record")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.add_patient_record()
            elif choice == '2':
                self.retrieve_patient_record()
            elif choice == '3':
                self.update_medical_record()
            elif choice == '4':
                self.delete_patient_record()
            elif choice == '5':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

system = HealthMonitoringSystem()
system.menu()