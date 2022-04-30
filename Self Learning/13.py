has_high_income = True
has_good_credit = False
has_criminal_record = True
if has_high_income and has_good_credit and not has_criminal_record:
    print('Eligible for loan')

elif has_high_income and not has_criminal_record or has_good_credit and not has_criminal_record:
    print('Tentitavly eligible for loan')

else:
    print('Not eligible for loan')



