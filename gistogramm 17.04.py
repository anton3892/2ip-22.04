# import matplotlib.pyplot as plt
# import numpy as np
#
# # x_axis = np.linspace(-10, -7, 100)
# # values = np.sin(x_axis)
# #
# # weights = (values + 1)  # для повторения ( 1 положительными для весов)
# # plt.figure(figsize=(10, 5))
# # plt.hist(x_axis, bins=100, weights=weights, edgecolor='black', alpha=0.7)
# #
# # plt.grid(True)
# # plt.show()
#
#
# # import matplotlib.pyplot as plt
# # import numpy as np
# #
# # Данные
# # volumes = [5, 10, 15, 23, 18, 12, 8, 14, 9, 7]
# # x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# # #
# # # # Создаём фигуру
# # fig, ax1 = plt.subplots(figsize=(10, 6))
# # #
# # # Вычисляем среднее для разделения цветов
# # mean_volume = np.mean(volumes)
# # colors = ['yellow' if vol > mean_volume else 'red' for vol in volumes]
# # # Строим столбцы
# # bars = ax1.bar(x_labels, volumes, color=colors, alpha=0.4)
# # # Настройка графика
# # ax1.set_ylabel('Объём', fontsize=12)
# # ax1.set_title('Объём торгов', fontsize=14)
# # ax1.grid(axis='y', alpha=0.3)
# # plt.tight_layout()
# #
# # # Отображаем график
# # plt.show()
#
#
#
#
# years = [2023,2024,2025,2026]
# Student1 = [3]
# Student2 = [3]
# Student3 = [3]
# Student4 = [3]
# Student5 = [3]
# res = 0
# # for i in Student1,Student2,Student3,Student4,Student5:
# #     if i == 3:
# #
# #         el:
# #         res +=1
#
#
#
#
#
#
# plt.stackplot(years,Student1,Student2,Student3,Student4,Student5,alpha = 0.7)
#
# plt.xlabel('Года')
# plt.ylabel('Студенты')
# plt.title('Успеваемость студентов за 2023-2024-2025-2026')
# plt.grid('true')
#
# plt.legend(loc='upper right')
#
# plt.show()
#



from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Примеры: ")
table.add_column("Года", style="cyan")
table.add_column("Титул", style="magenta")
table.add_row("2012", "Раз....")
table.add_row("2020", "Два....")

console.print(table)