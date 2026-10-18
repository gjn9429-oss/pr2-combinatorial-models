import random


def collision_probability(n, k):
    # Теоретична ймовірність відсутності колізії
    probability_no_collision = 1.0

    for i in range(k):
        probability_no_collision = probability_no_collision * (n - i) / n

    return 1 - probability_no_collision


def simulate_collisions(n, k, experiments):
    collision_count = 0

    for experiment in range(experiments):
        keys = []

        # Генеруємо ключі незалежно, повторення дозволені
        for i in range(k):
            key = random.randint(1, n)
            keys.append(key)

        # Множина залишає лише різні значення
        if len(set(keys)) < k:
            collision_count = collision_count + 1

    return collision_count / experiments


def main():
    n = 365
    experiments = 10000
    k_values = [5, 10, 15, 20, 23, 30, 40, 50, 60, 70, 80]

    print("Блок 1. Дослідження колізій")
    print(f"Можливих значень: {n}")
    print(f"Експериментів для кожного k: {experiments}")
    print(" k | Теоретична P | Частота W | Похибка")

    for k in k_values:
        probability = collision_probability(n, k)
        frequency = simulate_collisions(n, k, experiments)
        error = abs(frequency - probability)

        print(f"{k:2} | {probability:.6f}      | {frequency:.6f}  | {error:.6f}")


if __name__ == "__main__":
    main()
