from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    current_datetime = datetime.now()
    containers = []

    def SortWeekday(users):
        for user, date in users.items():
            date = datetime(year=current_datetime.year,
                            month=date.month, day=date.day)
            return date
    users.sort(key=SortWeekday)

    for user in users:
        name, birthday = user.popitem()
        birthday = datetime(year=current_datetime.year,
                            month=birthday.month, day=birthday.day)

        def containers_append() -> None:
            if birthday.weekday() == 5 or birthday.weekday() == 6:
                containers.append('Monday' + ': ' + name)
            else:
                containers.append(birthday.strftime('%A') + ': ' + name)

        if current_datetime.weekday() == 0:
            if current_datetime - timedelta(days=3) < birthday <= current_datetime + timedelta(days=4):
                containers_append()

        elif current_datetime.weekday() == 5:
            if current_datetime - timedelta(days=1) < birthday <= current_datetime + timedelta(days=6):
                containers_append()

        elif current_datetime.weekday() == 6:
            if current_datetime - timedelta(days=1) < birthday <= current_datetime + timedelta(days=5):
                containers_append()

        else:
            if current_datetime <= birthday <= current_datetime + timedelta(days=7):
                containers_append()

    containers_dict = defaultdict(list)
    for element in containers:
        e = element.split(': ')
        char = e[0]
        containers_dict[char].append(e[1])

    for weekday in dict(containers_dict):
        time_name_string = ''
        for name in dict(containers_dict)[weekday]:
            time_name_string += name + ', '
        names = time_name_string.removesuffix(', ')

        print(f'{weekday}: {names}')