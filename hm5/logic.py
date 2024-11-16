import random


def play_game(min_number, max_number, attempts, start_capital):
    capital = start_capital
    target_number = random.randint(min_number, max_number)

    print(f"Угадайте число от {min_number} до {max_number}!")

    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt}/{attempts}. Ваш капитал: {capital}")

        try:
            bet = int(input("Введите вашу ставку: "))
            if bet > capital:
                print("Ставка превышает ваш капитал!")
                continue

            guess = int(input("Введите ваш выбор: "))

            if guess < min_number or guess > max_number:
                print(f"Число должно быть в диапазоне от {min_number} до {max_number}.")
                continue

            if guess == target_number:
                capital += bet
                print(f"Поздравляем! Вы угадали число. Ваш капитал удвоен: {capital}")
                break
            else:
                capital -= bet
                print(f"Неверно. Осталось попыток: {attempts - attempt}. Ваш капитал: {capital}")

            if capital <= 0:
                print("Вы проиграли весь капитал!")
                break

        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")

    print(f"\nИгра завершена. Загаданное число было: {target_number}. Ваш капитал: {capital}")
    return capital