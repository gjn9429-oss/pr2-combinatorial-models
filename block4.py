import random

# Кожен рядок — значення чотирьох параметрів
test_scenarios = [
    (0, 0, 0, 0),
    (0, 1, 1, 1),
    (0, 2, 2, 2),
    (1, 0, 1, 2),
    (1, 1, 2, 0),
    (1, 2, 0, 1),
    (2, 0, 2, 1),
    (2, 1, 0, 2),
    (2, 2, 1, 0)
]

total = 3 ** 4
covered = len(test_scenarios)
probability = covered / total

print("Блок 4. Тестове покриття Pairwise")
print("Усього конфігурацій:", total)
print("Сценаріїв у наборі:", covered)
print(f"Теоретична ймовірність = {probability:.6f}")

experiments = 10000
hits = 0

for experiment in range(experiments):
    # Незалежно вибираємо значення чотирьох параметрів
    configuration = (
        random.randint(0, 2),
        random.randint(0, 2),
        random.randint(0, 2),
        random.randint(0, 2)
    )

    # Перевіряємо збіг усієї конфігурації зі сценарієм
    if configuration in test_scenarios:
        hits = hits + 1

frequency = hits / experiments
error = abs(frequency - probability)

print("\nРезультати симуляції")
print("Кількість експериментів:", experiments)
print("Збігів із тестовим набором:", hits)
print(f"Теоретична ймовірність = {probability:.6f}")
print(f"Статистична частота = {frequency:.6f}")
print(f"Абсолютна похибка = {error:.6f}")