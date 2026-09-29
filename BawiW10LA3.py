while True:
    print(f"{'':=^40}")
    print(f"{'PIN Verification System':^40}")
    print(f"{'':=^40}")
    PIN = input("Enter your PIN: ")
    correct_PIN = "1234"

    found = False

    if PIN == correct_PIN:
        found = True

    if found:
        print("Correct PIN! Access Granted.")
    else:
        print("Incorrect PIN! Access Denied.")

    again = input("Try again? (Y/N): ")

    if again.lower() == "y":
        continue
    elif again.lower() == "n":
        print(f"{'':=^40}")
        print(f"{'Program Ended!':^40}")
        print(f"{'Bawi Works':^40}")
        print(f"{'':=^40}")
        break
    else:
        print("Please enter Y or N.")

