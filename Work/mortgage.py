# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0


extra_payment_start_month = input('Enter the month to start extra payment: ')
extra_payment_start_month = int(extra_payment_start_month)
extra_payment_end_month = input('Enter the month to end extra payment: ')
extra_payment_end_month = int(extra_payment_end_month)
extra_payment = input('Enter the extra payment amount: ')
extra_payment = float(extra_payment)



while principal > 0:

    if principal < payment:
        payment = principal * (1+rate/12)# Adjust payment to remaining principal
        extra_payment = 0
    principal = principal * (1+rate/12) - payment
    if months >= extra_payment_start_month and months < extra_payment_end_month:
        principal -= extra_payment
        total_paid += payment + extra_payment
    else:
        total_paid += payment
    months += 1

    print(f'{months} {total_paid} {principal}')
    
print(f'Total paid {round(total_paid,1):,}')
print(f'Months', months)