import json
import os


INVENTORY_FILE = "inventory.json"

def load_inventory():

    with open(INVENTORY_FILE, "r") as f:
        data = json.load(f)

        if not isinstance(data, list):
            print("JSON format incorrect. Resetting inventory.")
            return []
        
        return data

def save_inventory():
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=4)

# Step 1: Create a list to store all items
inventory = load_inventory()

# Step 2: Function to add a new item
def add_item():
    item_id = input("Enter item ID: ")
    name = input("Enter item name: ")
    status = input("Enter item status (available/borrowed): ")

    item = {
        "id": item_id,
        "name": name,
        "status": status
    }

    inventory.append(item)
    save_inventory
    print(f"✅ Item '{name}' added successfully!\n")

# Step 3: Function to view all items
def view_items():
    if not inventory:
        print("📦 Inventory is empty.\n")
    else:
        print("\n--- Inventory List ---")
        for item in inventory:
            print(f"ID: {item['id']} | Name: {item['name']} | Status: {item['status']}")
        print()

# Step 4: Function to delete an item
def delete_item():
    item_id = input("Enter the item ID to delete: ")
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            print(f"🗑️ Item '{item['name']}' deleted successfully!\n")
            return
    print("❌ Item not found.\n")
    save_inventory()

# Step 5: Main menu
def main_menu():
    while True:
        print("=== Inventory Management System ===")
        print("1. Add New Item")
        print("2. View All Items")
        print("3. Delete an Item")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            print("👋 Goodbye! Exiting system...")
            break
        else:
            print("⚠️ Invalid choice. Please try again.\n")

# Step 6: Start the program
main_menu()
