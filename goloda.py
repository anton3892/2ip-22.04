import matplotlib.pyplot as plt

city = ['Респ. Марий Эл', 'Чувашская Респ.', 'Респ. Мордовия', 'Респ. Татарстан', 'Нижегородская обл.']

mariy_el = [679417, 677097, 676351, 672321, 669854, 666202]

chuvashia = [1217818, 1186909, 1183908, 1173177, 1167061, 1159768]

mordovia = [790197, 783552, 781440, 771373, 765891, 758895]

tatarstan = [3902000, 3907000, 3916000, 3930000, 4003063, 4016571]

nijegorod = [3135000, 3119000, 3102000, 3081000, 3060000, 3039421]

years = [2020, 2021, 2022, 2023, 2024, 2025]
razdelenie = [0, 0.2, 0, 0, 0]

for i in range(len(years)):
#Собираю данные за конкретный год
    data = [mariy_el[i], chuvashia[i], mordovia[i], tatarstan[i], nijegorod[i]]
    total = sum(data)

    plt.figure(figsize=(10, 8))

    plt.pie(
        data,
        labels=city,
        explode=razdelenie, #выдвижение сектора
        # shadow=True, #3d
        startangle=140, #Угол поворота всей диаграммы
        pctdistance=0.75, #Расстояние от центра круга до текста
        wedgeprops={ 'edgecolor': 'black'},
        autopct=lambda p: f'{int(p * total / 100):,}'.replace(',', ' ') + f'\n({p:.1f}%)'
    )

    plt.title(f'Распределение населения в {years[i]} году', fontsize=14, pad=30)
    plt.text(1.1, 1.1, f'Год: {years[i]}', fontsize=12, fontweight='bold')
    plt.show()