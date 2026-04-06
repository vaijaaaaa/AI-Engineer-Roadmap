good_credit = True
criminal_record = True

if good_credit and criminal_record:
    print("Allowed")
elif good_credit or criminal_record:
    print("Partially Allowed")
elif good_credit and not criminal_record:
    print("OK")