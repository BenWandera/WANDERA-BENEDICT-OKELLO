"""Bill Split Calculator using control structures in Python."""


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("Please enter a value greater than zero.\n")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.\n")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                print("Please enter a whole number greater than zero.\n")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")


def get_tip_rate():
    while True:
        print("Select tip percentage:")
        print("1. 10%")
        print("2. 15%")
        print("3. 20%")
        print("4. Custom")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            return 0.10
        if choice == "2":
            return 0.15
        if choice == "3":
            return 0.20
        if choice == "4":
            while True:
                try:
                    custom_rate = float(input("Enter custom tip percentage: ").strip())
                    if custom_rate < 0:
                        print("Tip percentage cannot be negative.\n")
                        continue
                    return custom_rate / 100
                except ValueError:
                    print("Invalid input. Please enter a number.\n")

        print("Invalid choice. Please select 1, 2, 3, or 4.\n")


def calculate_bill_split(total_bill, number_of_people, tip_rate):
    tip_amount = total_bill * tip_rate
    total_with_tip = total_bill + tip_amount
    amount_per_person = total_with_tip / number_of_people

    return {
        "total_bill": total_bill,
        "number_of_people": number_of_people,
        "tip_rate": tip_rate,
        "tip_amount": tip_amount,
        "total_with_tip": total_with_tip,
        "amount_per_person": amount_per_person,
    }


def print_receipt(details):
    print("\n=== Bill Split Receipt ===")
    print(f"Total bill amount: {details['total_bill']:.2f}")
    print(f"Number of people: {details['number_of_people']}")
    print(f"Tip percentage: {details['tip_rate'] * 100:.0f}%")
    print(f"Tip amount: {details['tip_amount']:.2f}")
    print(f"Total bill with tip: {details['total_with_tip']:.2f}")
    print(f"Each person's share: {details['amount_per_person']:.2f}")
    print("==========================\n")


def main():
    print("=== Bill Split Calculator ===")
    total_bill = get_positive_float("Enter total bill amount: ")
    number_of_people = get_positive_int("Enter number of people: ")
    tip_rate = get_tip_rate()

    details = calculate_bill_split(total_bill, number_of_people, tip_rate)
    print_receipt(details)


if __name__ == "__main__":
    main()
