import math
import random


def main():
    # Кількість паролів: 6 різних символів із 36
    total = math.perm(36, 6)

    # Подія A: усі 6 символів — літери
    count_a = math.perm(26, 6)

    # Подія B: дві цифри, потім чотири літери
    count_b = math.perm(10, 2) * math.perm(26, 4)

    p_a = count_a / total
    p_b = count_b / total

    # Події несумісні
    p_intersection = 0
    p_union = p_a + p_b
    p_not_a = 1 - p_a

    print("Блок 2. Парольна безпека. Варіант 1")
    print("Кількість можливих паролів:", total)
    print(f"P(A) = {p_a:.6f}")
    print(f"P(B) = {p_b:.6f}")
    print(f"P(A і B) = {p_intersection:.6f}")
    print(f"P(A або B) = {p_union:.6f}")
    print(f"P(не A) = {p_not_a:.6f}")
    # Алфавіт пароля: 10 цифр і 26 малих латинських літер
    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    alphabet = digits + letters

    experiments = 100000

    success_a = 0
    success_b = 0
    success_intersection = 0
    success_union = 0
    success_not_a = 0

    for experiment in range(experiments):
        # Вибираємо 6 символів без повторень
        password = random.sample(alphabet, 6)

        # Подія A: усі символи — літери
        is_a = True
        for symbol in password:
            if symbol not in letters:
                is_a = False

        # Подія B: перші два символи — цифри, решта — літери
        is_b = True
        for i in range(6):
            if i < 2:
                if password[i] not in digits:
                    is_b = False
            else:
                if password[i] not in letters:
                    is_b = False

        if is_a:
            success_a = success_a + 1

        if is_b:
            success_b = success_b + 1

        if is_a and is_b:
            success_intersection = success_intersection + 1

        if is_a or is_b:
            success_union = success_union + 1

        if not is_a:
            success_not_a = success_not_a + 1

    w_a = success_a / experiments
    w_b = success_b / experiments
    w_intersection = success_intersection / experiments
    w_union = success_union / experiments
    w_not_a = success_not_a / experiments

    print(f"\nРезультати {experiments} симуляцій")
    print("Подія | Теоретична P | Частота W | Похибка")

    print(f"A     | {p_a:.6f} | {w_a:.6f} | {abs(w_a - p_a):.6f}")
    print(f"B     | {p_b:.6f} | {w_b:.6f} | {abs(w_b - p_b):.6f}")
    print(f"A і B | {p_intersection:.6f} | {w_intersection:.6f} | {abs(w_intersection - p_intersection):.6f}")
    print(f"A або B | {p_union:.6f} | {w_union:.6f} | {abs(w_union - p_union):.6f}")
    print(f"Не A  | {p_not_a:.6f} | {w_not_a:.6f} | {abs(w_not_a - p_not_a):.6f}")

    print("\nПеревірка доповнення:")
    print(f"W(не A) = {w_not_a:.6f}")
    print(f"1 - W(A) = {1 - w_a:.6f}")


if __name__ == "__main__":
    main()
