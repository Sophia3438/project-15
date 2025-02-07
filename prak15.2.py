import random

# Типи дій у грі
ACTIONS: dict[int, str] = {0: "Камінь", 1: "Папір", 2: "Ножиці"}
VICTORIES: dict[str, str] = {
    "Камінь": "Ножиці",  # Камінь б'є ножиці
    "Папір": "Камінь",  # Папір б'є камінь
    "Ножиці": "Папір",  # Ножиці б'ють папір
}


def get_user_selection(actions: dict[int, str]) -> str:
    """Отримує вибір гравця та перевіряє коректність введення."""
    while True:
        try:
            choices = [f"{actions[action]}[{action}]" for action in actions]
            choices_str = ", ".join(choices)
            selection = int(input(f"Виберіть дію ({choices_str}): "))
            return actions[selection]
        except (ValueError, KeyError):
            print(
                f"Некоректний вибір. Введіть номер із діапазону [0, {len(actions) - 1}]."
            )


def get_computer_selection(actions: dict[int, str]) -> str:
    """Вибір комп'ютера."""
    return actions[random.randint(0, len(actions) - 1)]


def determine_winner(
    victories: dict[str, str], user_action: str, computer_action: str
) -> str:
    """Визначає переможця гри."""
    if user_action == computer_action:
        return f"Обидва вибрали {user_action}. Нічия!"
    elif computer_action == victories[user_action]:
        return f"{user_action} перемагає {computer_action}. Ви виграли!"
    else:
        return f"{computer_action} перемагає {user_action}. Ви програли!"


if __name__ == "__main__":
    print("Ласкаво просимо до гри 'Камінь, ножиці, папір'!")
    while True:
        user_choice = get_user_selection(ACTIONS)
        computer_choice = get_computer_selection(ACTIONS)
        print(f"\nВаш вибір: {user_choice}, вибір комп'ютера: {computer_choice}.")
        result = determine_winner(VICTORIES, user_choice, computer_choice)
        print(result)

        play_again = input("Грати ще раз? (y/n): ").strip().lower()
        if play_again != "y":
            print("Дякуємо за гру! До зустрічі!")
            break
