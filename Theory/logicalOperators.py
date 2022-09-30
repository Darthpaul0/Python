high_income = True
good_credit = False
criminal = True

# Both conditions are true
if high_income and good_credit:
    print("Loan granted")
else:
    print("You better search a job.")
print("*"*10)
# At least one condition are true
if high_income or good_credit:
    print("Loan granted")
else:
    print("You better search a job.")
print("*"*10)
# Using NOT
if high_income and not criminal:
    print("Loan granted")
else:
    print("You better search a job.")
print("*"*10)
