# Проект: Гра Камінь-Папір-Ножиці
# Опис: Це проста гра, де користувач грає проти комп'ютера у Камінь-Папір-Ножиці.
# Гра перевіряє правильність введення і дозволяє грати кілька раундів.

import random


# Функція для отримання вибору користувача
def get_user_choice():
    user_input = input("Введіть 'камінь', 'папір' або 'ножиці': ").lower()
    # Перевірка правильності введення
    while user_input not in ["камінь", "папір", "ножиці"]:
        print("Невірний ввід! Виберіть 'камінь', 'папір' або 'ножиці'.")
        user_input = input("Введіть 'камінь', 'папір' або 'ножиці': ").lower()
    return user_input


# Функція для отримання вибору комп'ютера
def get_computer_choice():
    return random.choice(["камінь", "папір", "ножиці"])


# Функція для визначення переможця
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Нічия!"
    elif (
        (user_choice == "камінь" and computer_choice == "ножиці")
        or (user_choice == "ножиці" and computer_choice == "папір")
        or (user_choice == "папір" and computer_choice == "камінь")
    ):
        return "Ви виграли!"
    else:
        return "Переміг комп'ютер!"


# Основний цикл гри
def play_game():
    print("Ласкаво просимо в гру Камінь-Папір-Ножиці!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Комп'ютер вибрав: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Запитуємо користувача, чи хоче він грати ще
        play_again = input("Хочете грати ще раз? (так/ні): ").lower()
        if play_again != "так":
            print("Дякуємо за гру!")
            break


# Запуск гри
if __name__ == "__main__":
    play_game()
