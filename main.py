

state = "Home"

print("Type the number of the event to change state. Type 'help' for options, 'quit' to exit.\n")

while True:
    if state == "Home":
        print("\n--- STATE: Home ---")
        print("You are at home.")
        events = {"1": "Study", "2": "Break"}
        print("1) Start studying")
        print("2) Take a break")

    elif state == "Study":
        print("\n--- STATE: Study ---")
        print("You are studying.")
        events = {"1": "Break", "2": "Sleep"}
        print("1) Take a break")
        print("2) Go to sleep")

    elif state == "Break":
        print("\n--- STATE: Break ---")
        print("You are on a break.")
        events = {"1": "Study", "2": "Sleep"}
        print("1) Go back to studying")
        print("2) Take a nap (sleep)")

    elif state == "Sleep":
        print("\n--- STATE: Sleep ---")
        print("You are sleeping.")
        events = {"1": "Break", "2": "Study"}
        print("1) Wake up and go on break")
        print("2) Wake up and start studying")

    else:
        state = "Home"
        continue

    choice = input("Enter event (1/2 or 'help'/'quit'): ").strip().lower()

    if choice == "quit":
        print("Goodbye!")
        break
    if choice == "help":
        print("Enter 1 or 2 to pick an event shown above.")
        continue

    if choice in events:
        new_state = events[choice]
        print(f"Event accepted: {choice} -> {new_state}")
        state = new_state
    else:
        print(f"Invalid event '{choice}'. State stays: {state}.")


