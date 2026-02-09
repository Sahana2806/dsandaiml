contacts = {
    "Asha": "9876543210",
    "Ravi": "9123456780",
    "Meena": "9988776655"
}
contacts["Kiran"] = "9012345678"
contacts["Ravi"] = "9000000000"
print("Asha's Number:", contacts.get("Asha"))
print("Rahul's Number:", contacts.get("Rahul", "Contact not found"))
print("\n--- Contact List ---")
for name, number in contacts.items():
    print(f"Contact: {name} | Phone: {number}")


