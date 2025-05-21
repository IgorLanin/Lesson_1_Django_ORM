import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

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