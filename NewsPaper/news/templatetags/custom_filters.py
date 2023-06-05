from django import template

register = template.Library()

CENSOR = ['тест1', 'тест2', 'тест3', 'тест4', 'тест']
SYMBOLS = ' ,.!?'

@register.filter()
def censor(value):
    #value = 'Привет ворлд, тест. Ты тест1, если поддерживаешь ТЕСТ2. Тест3 это ваше, тест4.'
    #print('======='*10)
    #print(value)      #для просмотра исходного текста в консоли


    if isinstance(value, str):          # разбиваем исходный текст на слова и символы (знаки препинания)
        temp_array = []
        temp_word = ''
        for ind, symbol in enumerate(value):
            if symbol not in SYMBOLS:
                temp_word = temp_word + symbol
                if ind == len(value) - 1:
                    temp_array.append(temp_word)
            else:
                if temp_word == '':
                    temp_array.append(symbol)
                else:
                    temp_array.append(temp_word)
                    temp_word = ''
                    temp_array.append(symbol)

        # print(temp_array)      #для просмотра разделённого списка слов в консоли

        for ind, word in enumerate(temp_array):  # проверяем состав нашего текста на наличие запрещённых слов
            if (word.lower() or word.upper()) in CENSOR:
                new_word = word[0] + ('*' * (len(word) - 1))  # и производим зацензуривание
                temp_array[ind] = new_word

        # print(temp_array)      #для просмотра отформатированного списка слов в консоли

        recovered_text = ''  # восстаналиваем исходный текст, добавляя зацензуренные слова
        for words in temp_array:
            recovered_text = recovered_text + words
        refreshed_text = recovered_text.strip()
        # print(refreshed_text)      #для просмотра восстановленного текста в консоли

        return f'{refreshed_text}'
    else:
        print('Текст не подлежит модерации, т.к. не является текстом!')
        return value

