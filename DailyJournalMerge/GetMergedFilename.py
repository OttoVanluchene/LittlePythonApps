import datetime

def get_week_file():
    today = datetime.datetime.today()
    week_file = today.strftime("%Y-W%U.md")
    return week_file