from datetime import datetime, timedelta


def is_friday() -> bool:
    return datetime.today().weekday() == 4
