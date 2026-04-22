
import matplotlib.pyplot as plt

students = ['Студент1', 'Студент2', 'Студент3', 'Студент4', 'Студент5']

grades = {
    'Студент1': [3.5, 3.8, 4.2],
    'Студент2': [4.8, 4.9, 5.0],
    'Студент3': [3.0, 3.2, 3.1],
    'Студент4': [4.2, 4.0, 4.5],
    'Студент5': [3.9, 4.1, 4.3]
}

years = [2023, 2024, 2025]

colors = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd', '#ff7f0e']

plt.figure(figsize=(10, 6))

for i, student in enumerate(students):
    plt.plot(years, grades[student], marker='o', label=student, color=colors[i], linewidth=2)

    for year, grade in zip(years, grades[student]):
        plt.text(year, grade + 0.05, f'{grade}', ha='center')

plt.title('Динамика среднего балла студентов за 3 года', fontsize=14, pad=20)
plt.xlabel('Учебный год')
plt.ylabel('Средний балл')
plt.xticks(years)
plt.ylim(2, 5.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.show()