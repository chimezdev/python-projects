#     Scenario
# Once upon a time there was a land - a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course - 
# their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was 
# evaluated using the following rule:

# if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents 
# (this was the so-called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.

# Your task is to write a tax calculator.
# It should accept one floating-point value: the income.
# Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you - you'll find it in the skeleton code in the editor.
# Note: this happy country never returns money to its citizens. If the calculated tax is less than zero, it only means no tax at all (the tax is equal to zero). Take this into consideration during your calculations.

# Look at the code in the editor - it only reads one input value and outputs a result, so you need to complete it with some smart calculations.

income = float(input("Enter the annual income: "))

#Write your code here.
if income <= 85528:
    tax = ((0.18 * income)- 556.2)
else:
    tax = (14839.2 + (0.32 * (income - 85528)))

if tax <= 0:
    tax = 0
else:
    tax = tax


tax = round(tax, 0)
print("The tax is:", tax, "thalers")