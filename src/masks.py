def get_mask_card_number(card_number: str)-> str:
    """маскирует номер карты"""
    card_number = card_number.replace(' ', '')
    if not card_number.isdigit() or len(card_number) != 16:
        return 'Неверный формат номера карты'

    #формируем маску

    first_n = card_number[:4]
    second_n = ' '+card_number[4:6]+'** '
    third_n = '**** '
    four_n = card_number[-4:]
    masked = first_n + second_n + third_n + four_n
    return masked
print(get_mask_card_number("1234567890123456"))

def get_mask_account(account_number: str)-> str:
    """маскирует счет на карте"""


    masked_acc = '**' + account_number[-4:]
    return masked_acc
print(get_mask_account('2000567'))


