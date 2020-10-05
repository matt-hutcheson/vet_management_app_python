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
    years = int(age)
    days_per_year = 365.24
    new_date = datetime.date.today() - datetime.timedelta(days=(years*days_per_year))
    if len(str(new_date.day)) < 2:
        if len(str(new_date.month)) < 2:
            dob = str(new_date.year) + "-0" + str(new_date.month) + "-0" + str(new_date.day)
        else:
            dob = str(new_date.year) + "-" + str(new_date.month) + "-0" + str(new_date.day)
    else:
        dob = str(new_date.year) + "-" + str(new_date.month) + "-" + str(new_date.day)
    return dob

def check_checked_in(check_in_date, check_out_date):
    if datetime.datetime.strptime(check_in_date, "%d/%m/%Y") < datetime.datetime.now() and datetime.datetime.now() < datetime.datetime.strptime(check_out_date, "%d/%m/%Y"):
        checked_in = True
    else:
        checked_in = False
    return checked_in