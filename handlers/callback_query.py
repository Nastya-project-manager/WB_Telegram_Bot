from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
import pandas as pd
import Parser

router = Router()


@router.callback_query(F.data.split(':')[0] == 'select')
async def callback_answer(query: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(callback_query_id=query.id, show_alert=True, text='Идет Анализ!')
    await query.message.delete()
    df = pd.read_csv('wildberries_menu.csv', usecols=['name', 'id', 'shard', 'query'])
    categori_id = int(query.data.split(':')[1])
    categori = df[df['id'] == categori_id]
    products = Parser.get_products(categori['name'].values[0],
                                   categori['shard'].values[0],
                                   categori['query'].values[0])
    result = Parser.analysis(products['products'])
    photo_url = Parser.check_urls_parallel(str(result['id']))
    # Создаем текст из DataFrame
    products_text = (f"🛒 <b>Название:</b> {result['name']}\n"
                     f"🎨 <b>Цвет:</b> {result['colors']}\n"
                     f"🏷️ <b>Бренд:</b> {result['brand']}\n"
                     f"⭐ <b>Рейтинг:</b> {result['rating']}\n"
                     f"💬 <b>Отзывы:</b> {result['feedbacks']}\n"
                     f"💵 <b>Средняя цена:</b> {result['average_price']} руб.\n"
                     f"📊 <b>Метрика качества:</b> {result['quality_metric']:.2f}\n"
                     f"🖥️ <b>Сыллка:</b> {result['url']}\n")
    if photo_url:
        await bot.send_photo(chat_id=query.message.chat.id,
                             photo=photo_url,
                             caption=products_text,
                             parse_mode='HTML')
    else:
        await bot.send_message(chat_id=query.message.chat.id, text=products_text,parse_mode='HTML')
