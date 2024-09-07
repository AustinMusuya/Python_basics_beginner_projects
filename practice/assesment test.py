#Assesment Test

#Check if item is eligible for 10% credit off or not.

price = 10000
has_credit = True
'''
Prepare an If else statement for if item is eligible for 10% or 20% credit,
or any other condition you may prepare.
if 10% eligible, print 10% price
else print 20% down-payment to pay for item credit price.
'''
price = 10000
has_credit = False

if has_credit:
    downpayment = 0.1 * price
else:
    downpayment = 0.2 * price
    print(f"downpayment:{downpayment}")

