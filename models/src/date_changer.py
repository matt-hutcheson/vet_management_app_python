def date_box_to_date(date):
    new_date = str(date[-2:]) + "/" + str(date[5:7]) + "/" + str(date[0:4])
    return new_date