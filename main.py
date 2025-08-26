from datetime import timezone
import os

import django
from django.utils.timezone import localtime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    employees = Passcard.objects.all()
    # print(employees)        # print(list(employees)) : для вывода всех пропусков

    some_employee = employees[1] # Breanna Campbell

    # Данные Breanna Campbell
    # print('owner_name: ', some_employee.owner_name)
    # print('passcode: ', some_employee.passcode)
    # print('created_at: ', some_employee.created_at)
    # print('is_active: ', some_employee.is_active)

    # Количество активных пропусков из 100 сотрудников через цикл
    # active_passcards = [employee for employee in employees if employee.is_active]
    # print('Активных пропусков: ', len(active_passcards))

    # Количество активных пропусков без цикла/list comprehension
    active_passcards = Passcard.objects.filter(is_active=True)
    print('Активных пропусков: ', len(active_passcards))

    # В хранилище
    # visits = Visit.objects.all()
    # print(visits)

    # Те, кто не вышли:
    no_leaved_visits = Visit.objects.filter(leaved_at=None)

    for no_leaved_visit in no_leaved_visits:
        print("Посетитель в хранилище: ", no_leaved_visit.passcard)
        # print("Зашел в хранилище, время по Москве: ", localtime(value=no_leaved_visit.entered_at, timezone=+3))

