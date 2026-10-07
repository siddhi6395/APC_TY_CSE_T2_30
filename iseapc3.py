data = {}

while True:
    print("\n1. Add | 2. Search | 3. Update | 4. Delete | 5. Show All | 6. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        p_id = input("Enter Patient ID: ")
        if p_id in data:
            print("ID already exists!")
        else:
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            disease = input("Enter Disease: ")
            data[p_id] = [name, age, disease]
            print("Patient added!")

    elif choice == "2":
        p_id = input("Enter ID to search: ")
        if p_id in data:
            patient = data[p_id]
            print(f"Name: {patient[0]}, Age: {patient[1]}, Disease: {patient[2]}")
        else:
            print("Not found!")

    elif choice == "3":
        p_id = input("Enter ID to update: ")
        if p_id in data:
            print("Enter new details:")
            name = input("New Name: ")
            age = input("New Age: ")
            disease = input("New Disease: ")
            data[p_id] = [name, age, disease]
            print("Updated successfully!")
        else:
            print("Not found!")

    elif choice == "4":
        p_id = input("Enter ID to delete: ")
        if p_id in data:
            del data[p_id]
            print("Deleted successfully!")
        else:
            print("Not found!")

    elif choice == "5":
        if not data:
            print("No records found.")
        for p_id, patient in data.items():
            print(f"ID: {p_id} -> Name: {patient[0]}, Age: {patient[1]}, Disease: {patient[2]}")

    elif choice == "6":
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice! Try again.")
