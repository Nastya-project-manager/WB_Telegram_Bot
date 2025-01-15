import pandas as pd
from aiogram.utils.keyboard import InlineKeyboardBuilder



def open_menu():
    df = pd.read_csv("wildberries_menu.csv", usecols=['name', 'id'])
    return df


def categories() -> InlineKeyboardBuilder.as_markup:
    """
    Функция, которая создает клавиатуру для выбора категорий
    :return:
    """
    markup = InlineKeyboardBuilder()
    for  _, row in open_menu().iterrows():
        markup.adjust(4)
        markup.button(text=row['name'], callback_data=f"select:{row['id']}")
    return markup.as_markup()


