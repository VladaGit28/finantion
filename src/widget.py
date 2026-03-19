from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime


def mask_account_card(card_info: str) -> str:
    """маскирует номер карты или счета в зависимости от типа"""
    # разделим строку на части
    parts = card_info.rsplit(sep=' ',maxsplit= 1)

    if len(parts) != 2:
        return 'Неверный формат данных'

    card_type = parts[0]
    card_number = parts[1]

    # определяем тип карты или счета и применяем соответствующую маскировку

    if card_type.lower() != 'счeт':
        # для карты используем маскировку номера карты
        masked_number = get_mask_card_number(card_number)
    else:
        # для счета используем маскировку счета
        masked_number = get_mask_account(card_type)

    return f'{card_type} {masked_number}'


def get_date(date_string: str) -> str:
    """преобразует дату из формата ISO в формат 'ДД.ММ.ГГ'"""
    try:
        # парсим iso в формат даты
        date_obj = datetime.fromisoformat(date_string)
        # форматируем в нужный формат
        return date_obj.strftime('%d.%m.%Y')
    except ValueError:
        return 'Неверный формат даты'


if __name__ == "__main__":
    print("Тестирование функций модуля widget:")
    print("-" * 40)

    # Тестируем для карты Maestro
    maestro_example = "Maestro 7000792289606361"
    print(f"mask_account_card('{maestro_example}')")
    print(f"Результат: {mask_account_card(maestro_example)}")
    print()

    # Тестируем для карты Visa Platinum
    visa_example = "Visa Platinum 7000792289606361"
    print(f"mask_account_card('{visa_example}')")
    print(f"Результат: {mask_account_card(visa_example)}")
    print()

    # Тестируем для счета
    account_example = "Счет 73654108430135874305"
    print(f"mask_account_card('{account_example}')")
    print(f"Результат: {mask_account_card(account_example)}")
    print()

    # Тестируем get_date
    date_example = "2024-03-11T02:26:18.671407"
    print(f"get_date('{date_example}')")
    print(f"Результат: {get_date(date_example)}")