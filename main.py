# main.py
class Loan:
    def __init__(self, amount, interest_rate, duration_years, compounding_frequency=12, additional_fee=0):
        self.amount = amount
        self.interest_rate = interest_rate
        self.duration_years = duration_years
        self.compounding_frequency = compounding_frequency
        self.additional_fee = additional_fee

    def calculate_monthly_payment(self):
        monthly_interest_rate = self.interest_rate / 100 / 12
        num_payments = self.duration_years * 12
        monthly_payment = (
            self.amount
            * monthly_interest_rate
            * (1 + monthly_interest_rate) ** num_payments
        ) / ((1 + monthly_interest_rate) ** num_payments - 1)
        return round(monthly_payment, 2)
    
    def calculate_total_repayment(self):
        num_payments = self.duration_years * self.compounding_frequency
        monthly_payment = self.calculate_monthly_payment()

        # Calculate total repayment, including additional fees
        total_repayment = monthly_payment * num_payments + self.additional_fee * self.duration_years
        return round(total_repayment, 2)

def main():
    loan_amount = float(input("Enter the loan amount: "))
    interest_rate = float(input("Enter the annual interest rate (%): "))
    duration_years = int(input("Enter the loan duration (in years): "))
    loan = Loan(loan_amount, interest_rate, duration_years)
    monthly_payment = loan.calculate_monthly_payment()

    print(f"\nMonthly Payment: ${monthly_payment}")

if __name__ == "__main__":
    main()
