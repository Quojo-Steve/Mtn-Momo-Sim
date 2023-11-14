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

starter_code = input("Welcome, type *170# to continue ")

def first_page():
    print("Menu\n 1) Transfer Money \n 2) MomoPay and Pay Bill \n 3) Airtime and Bundles \n 4) Allow Cash Out \n 5) Financial Services \n 6) My Wallet \n 7) Momo Promo" )
    option1 = input()
    if option1 == "1":
        transfer()


if starter_code == "*170#":
    first_page()
