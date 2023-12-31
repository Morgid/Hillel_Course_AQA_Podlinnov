# Задача 1
# Напишіть програму яка запитує в користувача вартість покупок, він їх вводе через пробіл,
# точна кількість не вказана. Вам потрібно до вартості покупок додати 6,5 відсотки податків.
# Потім питаєте чи є в користувача купон на знижку якщо є то питаєте це на суму чи на відсоток
# і потім віднімаєте суму або відсоток відповідно від ціни яку отримали раніше і пишете користувачу кінцеву суму.
# * завдання з зірочкою не впливає на бал.
# Округліть суму якщо копійок більше ніж 44 то це буде + 1 гривня, якщо менше.
# то тоді просто відкидаємо копійки від ціни.
#

print('Задача 1')
customer_bill = input("Введіть вартість покупок: ").split()
customer_bill = [float(i) for i in customer_bill]
print('Сума в чеку: ', sum(customer_bill))
tax = round(sum(customer_bill) * (6.5 / 100), 2)
print('Податок:', tax)
bill_with_tax = round(sum(customer_bill) + (sum(customer_bill) * (6.5 / 100)), 2)
print('До сплати: ', bill_with_tax)

discount = input('У вас є купон на знижку? (y/n): ')

if discount.lower() == 'y':
    discount_sum_percent = input('Знижка на суму чи на відсоток? (sum/per): ')

    if discount_sum_percent.lower() == 'sum':
        discount_customer = float(input('Введіть суму знижки: '))

        if discount_customer > bill_with_tax:
            print('Ваша знижка перевищує суму чека.', end='\nСума до сплати не може бути від`ємною!')

        else:
            discount_sum = int(bill_with_tax) - int(discount_customer)
            discount_sum_not_round = bill_with_tax - discount_customer
            round_sum_bill = round((discount_sum_not_round - discount_sum), 2)

            if round_sum_bill > 0.44:
                discount_sum = int(discount_sum) + 1
                print('Сума до сплати разом зі знижкою: ', discount_sum)

            if round_sum_bill == 0.44:
                print('Сума до сплати разом зі знижкою: ', discount_sum_not_round)

            if round_sum_bill < 0.44:
                discount_sum = int(discount_sum)
                print('Сума до сплати разом зі знижкою: ', discount_sum)

    if discount_sum_percent.lower() == 'per':
        percent = float(input('Веддіть відсоток знижки: '))
        percent_customer = bill_with_tax * (percent / 100)
        discount_customer_per = round((bill_with_tax - percent_customer), 2)

        if discount_customer_per < 0:
            print('Ваша знижка не може бути більше ніж 100%.', end='\nСума до сплати не може бути від`ємною!')

        else:
            round_per_bill = round(discount_customer_per - int(discount_customer_per), 2)

            if round_per_bill > 0.44:
                discount_percent = int(discount_customer_per) + 1
                print('Сума до сплати разом зі знижкою: ', discount_percent)

            if round_per_bill == 0.44:
                print('Сума до сплати разом зі знижкою: ', discount_customer_per)

            if round_per_bill < 0.44:
                discount_percent = int(discount_customer_per)
                print('Сума до сплати разом зі знижкою: ', discount_percent)

elif discount.lower() == 'n':
    print('До сплати: ', bill_with_tax)

else:
    print('Вкажіть на наявність купону y або n.')
