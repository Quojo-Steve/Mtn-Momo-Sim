def momo_user_transfer():
    print("Enter recipient's phone number:")
    recipient_number = input()
    print("Enter amount to transfer:")
    amount = int(input())
    print(f"You've sent {amount} to {recipient_number}")


def non_momo_user_transfer():
    print("Enter recipient's phone number:")
    recipient_number = input()
    print("Enter recipient's name:")
    recipient_name = input()
    print("Enter amount to transfer:")
    amount = int(input())
    print(f"You've sent {amount} to {recipient_number}")


def send_with_care():
    print("Enter recipient's phone number:")
    recipient_number = input()
    print("Enter amount to transfer:")
    amount = int(input())
    print(f"You've sent {amount} to {recipient_number}")


def transfer():
    print("Transfer Money\n 1) Momo User \n 2) Non Momo User \n 3) Send with Care \n 4) Favorite \n 5) Other Networks \n 6) Bank Account \n 0) Back")
    option2 = input()
    if option2 == "1":
        momo_user_transfer()
    elif option2 == "2":
        non_momo_user_transfer()
    elif option2 == "3":
        send_with_care()
    elif option2 == "0":
        first_page()
    else:
        print("Invalid option. Please try again.")
        transfer()

def momo_pay():
    print("MoMoPay\n 1) Pay Merchant \n 2) Pay Utility \n 3) Pay School Fees \n 0) Back")
    option3 = input()
    if option3 == "1":
        pay_merchant()
    elif option3 == "2":
        pay_utility()
    elif option3 == "3":
        pay_school_fees()
    elif option3 == "0":
        first_page()
    else:
        print("Invalid option. Please try again.")
        momo_pay()

def pay_merchant():
    print("Enter merchant's name:")
    merchant_name = input()
    print("Enter amount to pay:")
    amount = input()
    print(f"You've sent {amount} to {merchant_name}")


def pay_utility():
    print("Enter utility account number:")
    account_number = input()
    print("Enter amount to pay:")
    amount = input()
    print(f"You've sent {amount} to {account_number}")


def pay_school_fees():
    print("Enter student's name:")
    student_name = input()
    print("Enter school's name:")
    school_name = input()
    print("Enter amount to pay:")
    amount = input()
    print(f"You've sent {amount} to {school_name} for {student_name}")



def momo_and_pay_bill():
    print("MomoPay and Pay Bill\n 1) MoMoPay \n 2) Pay Bill \n 0) Back")
    option4 = input()
    if option4 == "1":
        momo_pay()
    elif option4 == "2":
        pay_bill()
    elif option4 == "0":
        first_page()
    else:
        print("Invalid option. Please try again.")
        momo_and_pay_bill()


starter_code = input("Welcome, type *170# to continue ")

def first_page():
    print("Menu\n 1) Transfer Money \n 2) MomoPay and Pay Bill \n 3) Airtime and Bundles \n 4) Allow Cash Out \n 5) Financial Services \n 6) My Wallet \n 7) Momo Promo" )
    option1 = input()
    if option1 == "1":
        transfer()
    elif option1 == "2":
        momo_and_pay_bill()


if starter_code == "*170#":
    first_page()

