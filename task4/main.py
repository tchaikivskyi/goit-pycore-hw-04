def parse_input(user_input):
    if not user_input.strip():
        return None, []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Use: add name and phone"
    name, phone = args
    contacts[name] = phone
    save_contacts(contacts)
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Use: change name and new_phone"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        save_contacts(contacts)
        return "Contact updated."
    return "Contact not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid input. Use: phone [name]"
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def save_contacts(contacts):
    with open("task4/contacts.txt", "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name} {phone}\n")


def load_contacts():
    contacts = {}
    try:
        with open("task4/contacts.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split()
                contacts[name] = phone
    except FileNotFoundError:
        print("File not found.")
    return contacts


def main():
    contacts = load_contacts()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue
        
        command, args = parse_input(user_input)
        if command is None:
            continue
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()