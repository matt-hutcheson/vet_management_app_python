from datetime import date as date_module
import datetime

def date_box_to_date(date):
    # 2020-08-01 to 01/08/2020
    new_date = str(date[-2:]) + "/" + str(date[5:7]) + "/" + str(date[0:4])
    return new_date

def date_to_date_box(date):
    # 01/08/2020 to 2020-08-01
    new_date = str(date[-4:]) + "-" + str(date[3:5]) + "-" + str(date[:2])
    return new_date

def date_to_age(date):
    # 19/08/2017 to 3
    age = int(((datetime.datetime.now() - datetime.datetime.strptime(date, "%d/%m/%Y")).days)/365.4)
    return age

def age_to_date(age):
    pass