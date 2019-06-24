print("How long will it take to put a down payment on your home?")

annual_salary = float(input("What is your annual salary? "))
portion_saved = float(input("What portion of your salary do you want to save, as a decimal? "))
total_cost = int(input("What is the cost of your dream home? "))

portion_down_payment = 0.25
down = total_cost * portion_down_payment
#
print 'You will need a downpayment of %d dollars' % (down)

current_savings = 0

monthly_saved = (annual_salary/12) * portion_saved

r = 0.04
growth = current_savings*r/12
compound = monthly_saved + growth
month = 0
while current_savings <= down:
    current_savings = current_savings + compound
    month += 1
print 'Number of months %d' % (month)
