import datetime


def yesterday():
    """Get yesterday's date"""
    yesterday_local = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday_year = str(yesterday_local.year)
    if yesterday_local.month < 10:
        yesterday_month = "0" + str(yesterday_local.month)
    else:
        yesterday_month = str(yesterday_local.month)
    if yesterday_local.day < 10:
        yesterday_day = "0" + str(yesterday_local.day)
    else:
        yesterday_day = str(yesterday_local.day)
    return yesterday_year, yesterday_month, yesterday_day


def today():
    """Get today's date"""
    now = datetime.datetime.now()
    current_year = str(now.year)
    if now.month < 10:
        current_month = "0" + str(now.month)
    else:
        current_month = str(now.month)
    if now.day < 10:
        current_day = "0" + str(now.day)
    else:
        current_day = str(now.day)
    return current_year, current_month, current_day


def tommorow():
    """Get tommorow's date"""
    tommorow_local = datetime.datetime.now() + datetime.timedelta(days=1)
    tommorow_year = str(tommorow_local.year)
    if tommorow_local.month < 10:
        tommorow_month = "0" + str(tommorow_local.month)
    else:
        tommorow_month = str(tommorow_local.month)
    if tommorow_local.day < 10:
        tommorow_day = "0" + str(tommorow_local.day)
    else:
        tommorow_day = str(tommorow_local.day)
    return tommorow_year, tommorow_month, tommorow_day


# print(yesterday())
# print(today())
# print(tommorow())
