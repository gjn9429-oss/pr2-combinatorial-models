import math
import random
import matplotlib.pyplot as plt
from pathlib import Path

# Координата перетину кривих
x0 = (math.sqrt(5) - 1) / 2

# Значення первісної на верхній і нижній межах
upper = 1 / 3 + 1 / 2 - 1
lower = x0 ** 3 / 3 + x0 ** 2 / 2 - x0

area = upper - lower

print("Блок 3. Геометрична ймовірність")
print(f"Точка перетину x0 = {x0:.6f}")
print(f"Площа області = {area:.9f}")
print(f"Теоретична ймовірність = {area:.9f}")

n_values = [100, 1000, 10000, 100000, 1000000]
frequencies = []

print("\n       N | Влучань M | Частота W | Похибка")

for n in n_values:
    hits = 0

    for i in range(n):
        # Незалежні рівномірні координати в одиничному квадраті
        x = random.random()
        y = random.random()

        if y <= x * x and y >= 1 - x:
            hits = hits + 1

    frequency = hits / n
    error = abs(frequency - area)
    frequencies.append(frequency)

    print(f"{n:8} | {hits:9} | {frequency:.6f}  | {error:.6f}")

# Папка для збереження графіка
graphics_folder = Path(__file__).parent / "graphics"
graphics_folder.mkdir(exist_ok=True)

plt.figure(figsize=(8, 5))

plt.plot(n_values, frequencies, marker="o", label="Статистична частота")
plt.axhline(area, color="red", linestyle="--", label="Теоретична ймовірність")

plt.xscale("log")
plt.xlabel("Кількість точок N")
plt.ylabel("Ймовірність")
plt.title("Блок 3. Збіжність оцінки методом Монте-Карло")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig(graphics_folder / "block3_convergence.png", dpi=200)
print("\nГрафік збережено: graphics/block3_convergence.png")

plt.show()
