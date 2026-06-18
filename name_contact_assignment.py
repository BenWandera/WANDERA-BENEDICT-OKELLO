import re

def validate_phone(phone):
    """Validate that phone contains only digits and hyphens."""
    if not re.match(r'^[0-9\-\+]+$', phone):
        print("Error: Phone number must contain only digits and hyphens (e.g., '+256-701').")
        return False
    return True

def validate_email(email):
    """Validate that email contains @ and a period."""
    if email and ('@' not in email or '.' not in email):
        print("Error: Email must contain '@' and '.' (e.g., 'user@example.com').")
        return False
    return True

contacts = {}

def add_contact(name, phone, email=""):
    if not validate_phone(phone):
        return
    if not validate_email(email):
        return
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")

def update_contact(name, phone=None, email=None):
    if name not in contacts:
        print(f"Error: Contact '{name}' not found.")
        return
    if phone:
        if not validate_phone(phone):
            return
        contacts[name]["phone"] = phone
    if email is not None:
        if not validate_email(email):
            return
        contacts[name]["email"] = email
    print(f"Contact '{name}' updated successfully.")

def format_contact_display(name, info):
    """Helper method to display a contact in a clean, user-friendly format."""
    print("\n" + "-" * 50)
    print(f"Name:  {name}")
    print(f"Phone: {info['phone']}")
    print(f"Email: {info['email'] if info['email'] else '(Not provided)'}")
    print("-" * 50)

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\n" + "=" * 50)
    print("ALL CONTACTS")
    print("=" * 50)
    for name, info in contacts.items():
        format_contact_display(name, info)

def search_contact(search_term):
    """Search contacts by name, phone, or email. Returns matching contacts."""
    if not search_term.strip():
        print("Error: Search term cannot be empty.")
        return
    
    search_term_lower = search_term.lower()
    results = []
    
    for name, info in contacts.items():
        if (search_term_lower in name.lower() or 
            search_term_lower in info['phone'] or 
            search_term_lower in info['email'].lower()):
            results.append((name, info))
    
    return results

def display_search_results(results, search_term):
    """Helper method to display search results in a clean format."""
    if not results:
        print(f"\nNo contacts found matching '{search_term}'.")
        return
    
    print("\n" + "=" * 50)
    print(f"SEARCH RESULTS FOR: '{search_term}'")
    print(f"Found {len(results)} contact(s)")
    print("=" * 50)
    
    for name, info in results:
        format_contact_display(name, info)

def delete_contact(name):
    if name not in contacts:
        print(f"Error: Contact '{name}' not found.")
        return
    del contacts[name]
    print(f"Contact '{name}' deleted successfully.")

def main():
    """
    Interactive Command Line Interface (CLI) for Contact Manager.
    Presents a recurring menu loop until the user chooses to exit.
    """
    while True:
        print("\n" + "="*40)
        print("CONTACT MANAGER")
        print("="*40)
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. View All Contacts")
        print("4. Search Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("="*40)
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            add_contact_menu()
        elif choice == '2':
            update_contact_menu()
        elif choice == '3':
            view_contacts()
        elif choice == '4':
            search_contact_menu()
        elif choice == '5':
            delete_contact_menu()
        elif choice == '6':
            print("\nThank you for using Contact Manager. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select 1-6.")

def add_contact_menu():
    """Get user input to add a new contact."""
    print("\n--- ADD CONTACT ---")
    name = input("Enter contact name: ").strip()
    
    if name in contacts:
        print(f"Error: Contact '{name}' already exists.")
        return
    
    phone = input("Enter phone number (e.g., '+256-701-123456'): ").strip()
    email = input("Enter email (optional, press Enter to skip): ").strip()
    
    add_contact(name, phone, email)

def update_contact_menu():
    """Get user input to update an existing contact."""
    print("\n--- UPDATE CONTACT ---")
    name = input("Enter contact name to update: ").strip()
    
    if name not in contacts:
        print(f"Error: Contact '{name}' not found.")
        return
    
    print(f"Current info - Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    
    update_choice = input("\nWhat would you like to update? (1=Phone, 2=Email, 3=Both): ").strip()
    
    phone = None
    email = None
    
    if update_choice in ('1', '3'):
        phone = input("Enter new phone number: ").strip()
    
    if update_choice in ('2', '3'):
        email = input("Enter new email: ").strip()
    
    update_contact(name, phone if phone else None, email if email else None)

def delete_contact_menu():
    """Get user input to delete a contact."""
    print("\n--- DELETE CONTACT ---")
    name = input("Enter contact name to delete: ").strip()
    delete_contact(name)

def search_contact_menu():
    """Get user input to search for contacts."""
    print("\n--- SEARCH CONTACT ---")
    search_term = input("Enter name, phone number, or email to search: ").strip()
    results = search_contact(search_term)
    display_search_results(results, search_term)

if __name__ == "__main__":
    main()