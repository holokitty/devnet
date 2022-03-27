import netmiko
frome netmiko import ConnectHandler

mikrotik_router_1 = {
    'device_type' = 'mikrotik_routeros',
    'host': '192.168.1.19',
    'port' = '22',
    'username' = 'admin+ct',
    'password' = '456',
}
sshCli = ConnectHandler(**mikrotik_router_1)

output = sshCli.send_command("/ip address print")

from prettytable import PrettyTable  # Импортируем установленный модуль.

# Определяем твою шапку и данные.
th = []
td = [...]

columns = len(th)  # Подсчитаем кол-во столбцов на будущее.

table = PrettyTable(th)  # Определяем таблицу.

# Cкопируем список td, на случай если он будет использоваться в коде дальше.
td_data = td[:]
# Входим в цикл который заполняет нашу таблицу.
# Цикл будет выполняться до тех пор пока у нас не кончатся данные
# для заполнения строк таблицы (список td_data).
while td_data:
    # Используя срез добавляем первые пять элементов в строку.
    # (columns = 5).
    table.add_row(td_data[:columns])
    # Используя срез переопределяем td_data так, чтобы он
    # больше не содержал первых 5 элементов.
    td_data = td_data[columns:]

print(table)  # Печатаем таблицу
print(output)
sshCli.disconnect()

