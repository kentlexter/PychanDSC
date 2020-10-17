high_income = False
good_credit = True
student = True
# If the first condition returns true or false, it stops evaluating the rest

if high_income and good_credit and not student:
    print("eligible")

if high_income or good_credit and not student:
    print("eligible")
