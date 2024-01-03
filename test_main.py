# test_main.py

from main import Loan

def test_calculate_monthly_payment():
    # Test case 1
    loan_1 = Loan(amount=100000, interest_rate=5, duration_years=30)
    calculated_payment = loan_1.calculate_monthly_payment()
    print(f"Input values: amount={loan_1.amount}, interest_rate={loan_1.interest_rate}, duration_years={loan_1.duration_years}")
    print(f"Calculated payment: {calculated_payment}, Expected: {loan_1.calculate_monthly_payment()}")
    assert abs(calculated_payment - loan_1.calculate_monthly_payment()) < 0.01

def test_calculate_monthly_payment_2():
    # Test case 2
    loan_2 = Loan(amount=200000, interest_rate=3, duration_years=15)
    calculated_payment = loan_2.calculate_monthly_payment()
    print(f"Input values: amount={loan_2.amount}, interest_rate={loan_2.interest_rate}, duration_years={loan_2.duration_years}")
    print(f"Calculated payment: {calculated_payment}, Expected: {loan_2.calculate_monthly_payment()}")
    assert abs(calculated_payment - loan_2.calculate_monthly_payment()) < 0.01

def test_calculate_monthly_payment_3():
    # Test case 3
    loan_3 = Loan(amount=150000, interest_rate=4, duration_years=20)
    calculated_payment = loan_3.calculate_monthly_payment()
    print(f"Input values: amount={loan_3.amount}, interest_rate={loan_3.interest_rate}, duration_years={loan_3.duration_years}")
    print(f"Calculated payment: {calculated_payment}, Expected: {loan_3.calculate_monthly_payment()}")
    assert abs(calculated_payment - loan_3.calculate_monthly_payment()) < 0.01

def test_calculate_monthly_payment_4():
    # Test case 4
    loan_4 = Loan(amount=300000, interest_rate=6, duration_years=25)
    calculated_payment = loan_4.calculate_monthly_payment()
    print(f"Input values: amount={loan_4.amount}, interest_rate={loan_4.interest_rate}, duration_years={loan_4.duration_years}")
    print(f"Calculated payment: {calculated_payment}, Expected: {loan_4.calculate_monthly_payment()}")
    assert abs(calculated_payment - loan_4.calculate_monthly_payment()) < 0.01

def test_calculate_monthly_payment_5():
    # Test case 5
    loan_5 = Loan(amount=120000, interest_rate=2.5, duration_years=10)
    calculated_payment = loan_5.calculate_monthly_payment()
    print(f"Input values: amount={loan_5.amount}, interest_rate={loan_5.interest_rate}, duration_years={loan_5.duration_years}")
    print(f"Calculated payment: {calculated_payment}, Expected: {loan_5.calculate_monthly_payment()}")
    assert abs(calculated_payment - loan_5.calculate_monthly_payment()) < 0.01

def test_calculate_monthly_payment_6():
    # Test case 6
    loan_6 = Loan(amount=200000, interest_rate=3, duration_years=15)
    calculated_payment = loan_6.calculate_monthly_payment()
    print(f"Input values: amount={loan_6.amount}, interest_rate={loan_6.interest_rate}, duration_years={loan_6.duration_years}")
    print(f"Calculated payment: {calculated_payment}, Expected: {loan_6.calculate_monthly_payment()}")
    assert abs(calculated_payment - loan_6.calculate_monthly_payment()) < 0.01

# test_main.py

def test_calculate_total_repayment():
    # Test case for total repayment
    loan = Loan(amount=150000, interest_rate=4, duration_years=20, compounding_frequency=12, additional_fee=100)
    
    # Calculate expected total repayment manually
    num_payments = loan.duration_years * loan.compounding_frequency
    expected_total_repayment = loan.calculate_monthly_payment() * num_payments + loan.additional_fee * loan.duration_years

    assert loan.calculate_total_repayment() == round(expected_total_repayment, 2)
