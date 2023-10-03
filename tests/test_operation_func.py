from src.operation_func import (filter_and_sorting, get_date, mask_prepare_message_number,
                                mask_card_number)


def test_get_date():
    assert get_date("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert get_date("2044-12-22****************") == "22.12.2044"


def test_mask_card_number():
    assert mask_card_number("4321765432168765") == "4321 76** **** 8765"


def test_mask_prepare_message_number_for_account():
    assert mask_prepare_message_number("Счет 12345678") == "Счет 12345678 **5678"


def test_mask_prepare_message_number_for_card():
    assert mask_prepare_message_number("Card 4321765432168765") == "Card 4321765432168765 4321 76** **** 8765"


def test_message_none():
    assert mask_prepare_message_number(None) == 'Personal account'


def test_filter_and_sorting_with_executed_states():
    data = [
        {'state': 'PENDING', 'date': '2023-10-01'},
        {'state': 'EXECUTED', 'date': '2023-09-30'},
        {'state': 'EXECUTED', 'date': '2023-09-29'},
        {'state': 'PENDING', 'date': '2023-09-28'},
    ]

    expected_result = [
        {'state': 'EXECUTED', 'date': '2023-09-30'},
        {'state': 'EXECUTED', 'date': '2023-09-29'},
    ]

    result = filter_and_sorting(data)
    assert result == expected_result
