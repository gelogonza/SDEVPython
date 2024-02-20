import emoji

def calculate_tip(bill_amount, tip_percentage):
    tip_amount = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip_amount
    return tip_amount, total_amount

def main():
    print("Welcome to the Tip Calculator!")
    bill_amount = float(input("Enter the total bill amount: $"))
    tip_percentage = float(input("Enter the tip percentage you would like to give: "))
    
    tip_amount, total_amount = calculate_tip(bill_amount, tip_percentage)
    
    print("\nCalculating tip...")
    print(emoji.emojize(f"\nThe tip amount is: ${tip_amount:.2f} :money_with_wings:"))
    print(emoji.emojize(f"The total amount to be paid is: ${total_amount:.2f} :money_bag:"))

if __name__ == "__main__":
    main()
