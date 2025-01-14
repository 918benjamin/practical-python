# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000


while principal > 0:
    current_payment = payment
    if (months > extra_payment_start_month and months < extra_payment_end_month):
        current_payment += extra_payment
    if (current_payment > principal):
        current_payment = principal * (1 + rate / 12)
    principal = principal * (1 + rate / 12) - current_payment
    total_paid = total_paid + current_payment
    months += 1
    print(f"{months} {total_paid} {principal}")
print(f'Total paid: {total_paid}\nTotal months: {months}')