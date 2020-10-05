def date_box_to_date(date):
    # 2020-08-01 to 01/08/2020
    new_date = str(date[-2:]) + "/" + str(date[5:7]) + "/" + str(date[0:4])
    return new_date

def date_to_date_box(date):
    # 01/08/2020 to 2020-08-01
    new_date = str(date[-4:]) + "-" + str(date[3:5]) + "-" + str(date[:2])
    return new_date