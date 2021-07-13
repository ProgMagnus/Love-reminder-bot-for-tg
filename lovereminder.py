import telebot
from telebot import types
import random
import time

bot = telebot.TeleBot("TOKEN")

level_one = ['Самое время подарить букет!', 'Пора бы сводить свою девушку в ресторан', 'Как насчет романтического ужина, бро?']
level_two = ['Купи шоколадку для своей любимой','Самое время подарить цветок', ' Готов поспорить, что твоя девушка не откажется от пирожного', 'Любовь это подарить жвачку love is']
level_three = ['Пора сказать как ты любишь свою девушку', 'Отправь стих любимой', 'Твоя девушка самая лучшая! Вот и напомни ей об этом']



class BotRunning:
	running = True

br = BotRunning()

@bot.message_handler(commands=['help'])
def help_welcome(message):
	bot.send_message(message.from_user.id,'У меня есть три уровня заботы\nЧем выше уровень, тем более серьезные жесты будут предложены к реализации\nДля выбора уровня заботы напиши /choice')

@bot.message_handler(commands=['stop'])
def stop_msg(message):
	bot.send_message(message.from_user.id, 'Напоминания приостановлены')
	br.running = False

@bot.message_handler(commands=['choice', 'start'])
def choice_msg(message):
	br.running = True
	keyboard = types.InlineKeyboardMarkup() 
	key_high = types.InlineKeyboardButton(text='Высокий уровень', callback_data='high_level')
	keyboard.add(key_high)
	key_medium = types.InlineKeyboardButton(text='Средний уровень', callback_data='medium_level')
	keyboard.add(key_medium)
	key_low = types.InlineKeyboardButton(text='Низкий уровень', callback_data='low_level')
	keyboard.add(key_low)
	key_stop = types.InlineKeyboardButton(text='Остановить напоминания', callback_data='stop_level')
	keyboard.add(key_stop)
	bot.send_message(message.from_user.id, text='Выбери уровень заботы', reply_markup=keyboard)


@bot.message_handler(content_types = ['text'])
def get_some_msg(message):
	if message.text !=' ':
		bot.send_message(message.from_user.id,'Напиши /help чтобы узнать как меня использовать')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	while br.running:
		if call.data == 'high_level':
				timer_one_lvl = random.randint(3600, 14400)
				time.sleep(timer_one_lvl)
				take_lvl_one = random.choice(level_one)
				bot.send_message(call.message.chat.id, take_lvl_one)
		elif call.data == 'medium_level':
				timer_two_lvl = random.randint(3600, 14400)
				time.sleep(timer_two_lvl)
				take_lvl_two = random.choice(level_two)
				bot.send_message(call.message.chat.id, take_lvl_two)
		elif call.data == 'low_level':
				timer_three_lvl = random.randint(3600, 14400)
				time.sleep(timer_three_lvl)
				take_lvl_three = random.choice(level_three)
				bot.send_message(call.message.chat.id, take_lvl_three)
		elif call.data == 'stop_level':
				bot.send_message(call.message.chat.id, 'Напоминания приостановлены')
				br.running = False

bot.polling(none_stop=True)


