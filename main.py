def main():
    print("================================")
    print("       EXPENSE TRACKER")
    print("================================")
    print()
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")
    print()

    choice = input("Choose an option: ")

    if choice == "1":
        print("Add expense selected.")
    elif choice == "2":
        print("View expenses selected.")
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
