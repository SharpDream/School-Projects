# Define a dictionary to store notes
notes = {}

# Main loop for the note-taking app
while True:
    print("\nOptions:")
    print("1. Add a note")
    print("2. View a note")
    print("3. Delete a note")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        notes[title] = content
        print("Note added successfully!")
    elif choice == "2":
        if not notes:
            print("No notes available.")
        else:
            print("Available notes:")
            for title in notes:
                print("- ", title)
            note_title = input("Enter note title to view: ")
            if note_title in notes:
                print("Note:", notes[note_title])
            else:
                print("Note not found.")
    elif choice == "3":
        if not notes:
            print("No notes available.")
        else:
            print("Available notes:")
            for title in notes:
                print("- ", title)
            note_title = input("Enter note title to delete: ")
            if note_title in notes:
                del notes[note_title]
                print("Note deleted successfully!")
            else:
                print("Note not found.")
    elif choice == "4":
        print("Exiting the note-taking app.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
