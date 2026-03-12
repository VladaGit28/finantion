from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(card_info: str)-> str:
    """маскирует номер карты или счета в зависимости от типа"""
    #разделим строку на части
    parts = card_info.rsplit(' ', 1)

    if len(parts) != 2:
        return 'Неверный формат данных'

    card_type = parts[0]
    card_number = parts[1]

    #определяем тип карты или счета и применяем соответствующую маскировку

    if card_type.lower() == 'счёт':
        #для счета используем маскировку счета
        masked_number = get_mask_account(card_number)
    else:
        #для карты используем маскировку номера карты
        masked_number = get_mask_card_number(card_number)
    return f'{card_type} {card_number}'

