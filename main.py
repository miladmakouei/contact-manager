# Contact Manager
# Python Automation Learning Project

FILE_NAME = "contacts.txt"


def load_contacts():
    contacts = []

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split("|")

                if len(parts) == 3:
                    contact = {
                        "name": parts[0],
                        "phone": parts[1],
                        "email": parts[2]
                    }

                    contacts.append(contact)

    except FileNotFoundError:
        pass

    return contacts


def save_contacts(contacts):

    with open(FILE_NAME, "w") as file:

        for contact in contacts:
            line = (
                f"{contact['name']}|"
                f"{contact['phone']}|"
                f"{contact['email']}\n"
            )

            file.write(line)


def show_contacts(contacts):

    if not contacts:
        print("\nNo contacts found.")
        return

    print("\n========== CONTACTS ==========")

    for contact in contacts:

        print(
            f"Name: {contact['name']} | "
            f"Phone: {contact['phone']} | "
            f"Email: {contact['email']}"
        )


def add_contact(contacts):

    print("\n========== ADD CONTACT ==========")

    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    existing_phones = set()

    for contact in contacts:
        existing_phones.add(contact["phone"])

    if phone in existing_phones:
        print("This phone number already exists.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

    save_contacts(contacts)

    print("Contact added successfully.")


def search_contact(contacts):

    search = input("\nEnter name or phone: ").strip().lower()

    found = False

    for contact in contacts:

        if (
            search in contact["name"].lower()
            or search in contact["phone"]
        ):

            print("\n---------- CONTACT FOUND ----------")

            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")

            found = True
            break

    if not found:
        print("Contact not found.")


def delete_contact(contacts):

    phone = input("\nEnter phone number to delete: ").strip()

    for contact in contacts:

        if contact["phone"] == phone:

            contacts.remove(contact)

            save_contacts(contacts)

            print("Contact deleted successfully.")

            return

    print("Contact not found.")


def main():

    contacts = load_contacts()

    while True:

        print("\n========== CONTACT MANAGER ==========")
        print("1. Show contacts")
        print("2. Add contact")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")
        print("=====================================")

        choice = input("Choose an option: ")

        if choice == "1":

            show_contacts(contacts)

        elif choice == "2":

            add_contact(contacts)

        elif choice == "3":

            search_contact(contacts)

        elif choice == "4":

            delete_contact(contacts)

        elif choice == "5":

            print("Goodbye!")
            break

        else:

            print("Invalid option. Please choose 1-5.")


try:
    main()

except KeyboardInterrupt:
    print("\nProgram stopped.")