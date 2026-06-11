# E-commerce app with login, discounts, coupons, and tax


USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "customer": {"password": "customer123", "role": "Customer"},
    "cashier": {"password": "cashier123", "role": "Cashier"},
}


COUPONS = {
    "SAVE10": 0.10,
    "SAVE20": 0.20,
    "VIP30": 0.30,
}


TAX_RATES = {
    "uganda": 0.18,
    "kenya": 0.16,
    "tanzania": 0.15,
    "rwanda": 0.14,
}


def login():
    print("\n=== Login ===")
    username = input("Username: ").strip().lower()
    password = input("Password: ").strip()

    if username in USERS:
        if password == USERS[username]["password"]:
            role = USERS[username]["role"]
            print(f"Welcome, {role}!\n")
            return role
        print("Wrong password.\n")
        return None

    print("User not found.\n")
    return None


def get_tax_rate(location):
    loc = location.strip().lower()
    return TAX_RATES.get(loc, 0.12)


def get_subtotal_discount(subtotal):
    # Tiered discounts based on amount
    if subtotal >= 1000:
        return 0.15
    if subtotal >= 500:
        return 0.10
    if subtotal >= 200:
        return 0.05
    return 0


def get_coupon_discount(coupon_code):
    coupon_code = coupon_code.strip().upper()
    if coupon_code in COUPONS:
        return COUPONS[coupon_code], True
    return 0.0, False


def calculate_final_price(subtotal, location, coupon_code):
    # Apply subtotal discount
    sub_disc_rate = get_subtotal_discount(subtotal)
    sub_disc = subtotal * sub_disc_rate
    after_sub = subtotal - sub_disc

    # Apply coupon
    coupon_rate, valid = get_coupon_discount(coupon_code)
    coupon_disc = after_sub * coupon_rate
    after_coupon = after_sub - coupon_disc

    # Add tax
    tax_rate = get_tax_rate(location)
    tax = after_coupon * tax_rate
    final = after_coupon + tax

    return {
        "subtotal": subtotal,
        "subtotal_discount_rate": sub_disc_rate,
        "subtotal_discount": sub_disc,
        "coupon_discount_rate": coupon_rate,
        "coupon_discount": coupon_disc,
        "coupon_valid": valid,
        "tax_rate": tax_rate,
        "tax_amount": tax,
        "final_price": final,
    }


def display_summary(details):
    print("=== Order Summary ===")
    print(f"Subtotal: {details['subtotal']:.2f}")
    print(f"Subtotal discount: {details['subtotal_discount_rate'] * 100:.0f}%")
    print(f"Subtotal discount amount: {details['subtotal_discount']:.2f}")

    if details["coupon_valid"]:
        print(f"Coupon discount: {details['coupon_discount_rate'] * 100:.0f}%")
        print(f"Coupon discount amount: {details['coupon_discount']:.2f}")
    else:
        print("Coupon code: invalid")
        print("Coupon discount amount: 0.00")

    print(f"Tax rate: {details['tax_rate'] * 100:.0f}%")
    print(f"Tax amount: {details['tax_amount']:.2f}")
    print(f"Final price: {details['final_price']:.2f}")


def admin_menu():
    print("\n=== Admin Menu ===")
    print("1. Calculate order")
    print("2. View users")
    print("3. Exit")

def customer_menu():
    print("\n=== Customer Menu ===")
    print("1. Calculate order")
    print("2. Exit")

def cashier_menu():
    print("\n=== Cashier Menu ===")
    print("1. Calculate order")
    print("2. Exit")


def process_order():
    try:
        subtotal = float(input("Enter subtotal amount: "))
        if subtotal <= 0:
            print("Must be greater than zero.\n")
            return
    except ValueError:
        print("Invalid number.\n")
        return

    location = input("Enter location (Uganda, Kenya, Tanzania, Rwanda): ")
    coupon_code = input("Enter coupon code (or press Enter if none): ")

    details = calculate_final_price(subtotal, location, coupon_code)
    display_summary(details)
    print()


def view_users():
    print("=== Registered Users ===")
    for username, info in USERS.items():
        print(f"{username} -> {info['role']}")
    print()


def run_role_menu(role):
    while True:
        if role == "Admin":
            admin_menu()
            choice = input("Choice: ").strip()
            if choice == "1":
                process_order()
            elif choice == "2":
                view_users()
            elif choice == "3":
                break
            else:
                print("Invalid.\n")
        elif role == "Customer":
            customer_menu()
            choice = input("Choice: ").strip()
            if choice == "1":
                process_order()
            elif choice == "2":
                break
            else:
                print("Invalid.\n")
        elif role == "Cashier":
            cashier_menu()
            choice = input("Choice: ").strip()
            if choice == "1":
                process_order()
            elif choice == "2":
                break
            else:
                print("Invalid.\n")


def main():
    role = login()
    if role:
        run_role_menu(role)


if __name__ == "__main__":
    main()