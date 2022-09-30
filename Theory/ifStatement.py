is_hot = False
is_cold = False
if is_hot:
    print("It's hot.")
elif is_cold:
    print("It's cold.")
else:
    print("It's a good day.")
print("*"*10)

price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = price*.1
else:
    down_payment = price*.2
print(f'${down_payment}')
