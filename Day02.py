from decimal import Decimal, ROUND_HALF_UP

class TipCalculator:
    def __init__(self, bill, tip_percent, people):
        self.bill = Decimal(bill)
        self.tip_percent = Decimal(tip_percent)
        self.people = people

    def calculate_total_tip(self):
        return self.bill * (self.tip_percent / 100)

    def calculate_total_bill(self):
        return self.bill + self.calculate_total_tip()

    def calculate_bill_per_person(self):
        total_bill = self.calculate_total_bill()
        bill_per_person = total_bill / self.people
        return bill_per_person.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def main():
    print("Welcome to the advanced tip calculator!")
    
    try:
        bill = Decimal(input("What was the total bill? ₹"))
        tip = Decimal(input("How much tip would you like to give? (in percentage) "))
        people = int(input("How many people to split the bill? "))
        
        if bill < 0:
            raise ValueError("Bill amount cannot be negative.")
        if tip < 0:
            raise ValueError("Tip percent must be non-negative.")
        if people <= 0:
            raise ValueError("Number of people must be greater than 0.")

        calculator = TipCalculator(bill, tip, people)
        final_amount = calculator.calculate_bill_per_person()
        print(f"Each person should pay: ₹{final_amount}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
        print("Please enter valid numerical values for the bill, tip, and number of people.")

if __name__ == "__main__":
    main()
