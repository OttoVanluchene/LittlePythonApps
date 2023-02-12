import datetime

def get_week_days():
    today = datetime.datetime.today()
    monday = today - datetime.timedelta(days=today.weekday())
    week_days = []
    for i in range(7):
        day = monday + datetime.timedelta(days=i)
        week_days.append(day.strftime("%Y-%m-%d") + ".md")
    return week_days